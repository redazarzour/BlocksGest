package com.example.quranloopplayer;

import android.content.SharedPreferences;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View; // Import for View, used by OnClickListener
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import java.io.IOException;

/**
 * MainActivity is the primary screen of the QuranLoopPlayer application.
 * It handles playback of a Quran recitation audio file with looping and
 * persists the playback position across app sessions.
 */
public class MainActivity extends AppCompatActivity {

    // MediaPlayer instance for handling audio playback.
    private MediaPlayer mediaPlayer;
    // Button to control play and pause functionality.
    private Button playPauseButton;
    // TAG for logging, helps in debugging.
    private static final String TAG = "MainActivity";
    // Name for SharedPreferences file to store app preferences.
    private static final String PREFS_NAME = "QuranLoopPlayerPrefs";
    // Key for storing the last playback position in SharedPreferences.
    private static final String KEY_LAST_POSITION = "lastPlaybackPosition";

    /**
     * Called when the activity is first created.
     * This is where most initialization should go: calling setContentView(int) to inflate
     * the activity's UI, using findViewById(int) to programmatically interact with widgets
     * in the UI, and setting up the MediaPlayer.
     * @param savedInstanceState If the activity is being re-initialized after previously
     *                           being shut down then this Bundle contains the data it most
     *                           recently supplied in onSaveInstanceState(Bundle).
     *                           Note: Otherwise it is null.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Set the user interface layout for this Activity
        // The layout file is defined in res/layout/activity_main.xml
        setContentView(R.layout.activity_main);

        // Initialize the play/pause button from the layout
        playPauseButton = findViewById(R.id.playPauseButton);
        // Create a new MediaPlayer instance
        mediaPlayer = new MediaPlayer();

        // Construct the URI for the audio resource.
        // This points to a raw resource file (e.g., an MP3) that should be placed in res/raw.
        // TODO: If R.raw.quran_recitation cannot be resolved during compilation,
        //  replace R.raw.quran_recitation with the string "quran_recitation"
        //  and ensure the MP3 file is correctly named and placed in res/raw.
        //  Example for string: Uri mediaPath = Uri.parse("android.resource://" + getPackageName() + "/raw/quran_recitation");
        //  For now, we will attempt to use R.raw.quran_recitation directly.
        Uri mediaPath = Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.quran_recitation);

        try {
            // Set the data source for the MediaPlayer. This specifies the audio file to be played.
            mediaPlayer.setDataSource(getApplicationContext(), mediaPath);
        } catch (IOException e) {
            // Log an error and disable the play/pause button if the data source cannot be set.
            Log.e(TAG, "Error setting data source: " + e.getMessage());
            playPauseButton.setEnabled(false); // Disable button as playback is not possible.
            // Consider showing a user-friendly error message (e.g., Toast).
            return; // Exit onCreate if MediaPlayer setup fails critically.
        }

        // Configure the MediaPlayer to loop the audio playback.
        mediaPlayer.setLooping(true);

        // Set a listener to be notified when the MediaPlayer is prepared for playback.
        // Preparation is an asynchronous process.
        mediaPlayer.setOnPreparedListener(new MediaPlayer.OnPreparedListener() {
            /**
             * Called when the media file is ready for playback.
             * @param mp The MediaPlayer that is prepared.
             */
            @Override
            public void onPrepared(MediaPlayer mp) {
                Log.d(TAG, "MediaPlayer prepared. Can start playback.");
                // Enable the play/pause button as the media is ready.
                playPauseButton.setEnabled(true);
                
                // Load the last saved playback position from SharedPreferences.
                SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
                int lastPosition = prefs.getInt(KEY_LAST_POSITION, 0); // Default to 0 if not found.
                if (lastPosition > 0) {
                    // If a valid last position exists, seek the MediaPlayer to that position.
                    Log.d(TAG, "Restoring playback to position: " + lastPosition);
                    mediaPlayer.seekTo(lastPosition);
                    // Optional: Auto-play if desired when restoring position.
                    // mediaPlayer.start();
                    // playPauseButton.setText("Pause");
                    // Current behavior: Seek only, user must press play.
                }
            }
        });

        // Set a listener to be notified of errors during playback.
        mediaPlayer.setOnErrorListener(new MediaPlayer.OnErrorListener() {
            /**
             * Called to indicate an error.
             * @param mp The MediaPlayer the error pertains to.
             * @param what The type of error that has occurred.
             * @param extra An extra code, specific to the error.
             * @return True if the method handled the error, false if it didn't.
             *         Returning false, or not having an OnErrorListener, will cause the
             *         OnErrorCompletionListener to be called.
             */
            @Override
            public boolean onError(MediaPlayer mp, int what, int extra) {
                Log.e(TAG, "MediaPlayer error - what: " + what + " extra: " + extra);
                // Disable the play/pause button on error to prevent further interaction with a faulty MediaPlayer.
                playPauseButton.setEnabled(false);
                // Returning true indicates that we've handled the error.
                return true;
            }
        });

        // Prepare the MediaPlayer for playback asynchronously.
        // The OnPreparedListener will be called when preparation is complete.
        mediaPlayer.prepareAsync();
        Log.d(TAG, "MediaPlayer setup initiated with prepareAsync.");

        // Set the OnClickListener for the play/pause button.
        playPauseButton.setOnClickListener(new View.OnClickListener() {
            /**
             * Called when the play/pause button is clicked.
             * @param v The view that was clicked (the button).
             */
            @Override
            public void onClick(View v) {
                // Check if MediaPlayer is initialized and currently playing.
                if (mediaPlayer != null && mediaPlayer.isPlaying()) {
                    // If playing, pause the MediaPlayer and update button text to "Play".
                    mediaPlayer.pause();
                    playPauseButton.setText("Play");
                    Log.d(TAG, "MediaPlayer paused.");
                } else if (mediaPlayer != null) {
                    // If not playing (and initialized), start the MediaPlayer and update button text to "Pause".
                    // This also handles resuming from a paused state.
                    // The button is typically disabled until onPrepared, so this check is an additional safeguard.
                    mediaPlayer.start();
                    playPauseButton.setText("Pause");
                    Log.d(TAG, "MediaPlayer started.");
                }
            }
        });
        Log.d(TAG, "onCreate completed.");
    }

    /**
     * Called when the activity is going into the background, but has not yet been killed.
     * This is a good place to save any state that needs to persist.
     */
    @Override
    protected void onPause() {
        super.onPause();
        Log.d(TAG, "onPause called.");
        if (mediaPlayer != null) {
            // Save the current playback position if the MediaPlayer is playing or has a valid position.
            // This ensures the position is remembered even if the user manually paused.
            int currentPosition = mediaPlayer.getCurrentPosition();
            if (currentPosition > 0 || mediaPlayer.isPlaying()) {
                 SharedPreferences.Editor editor = getSharedPreferences(PREFS_NAME, MODE_PRIVATE).edit();
                 editor.putInt(KEY_LAST_POSITION, currentPosition);
                 editor.apply(); // Use apply() for asynchronous saving.
                 Log.d(TAG, "Saved playback position: " + currentPosition);
            }

            // If the MediaPlayer is playing, pause it when the activity is paused.
            // This is important for good user experience and resource management.
            if (mediaPlayer.isPlaying()) {
                mediaPlayer.pause();
                playPauseButton.setText("Play"); // Update button text to reflect paused state.
                Log.d(TAG, "MediaPlayer paused in onPause.");
            }
        }
    }

    /**
     * Called before the activity is destroyed.
     * This is the final call that the activity receives.
     * It's crucial to release resources here to prevent memory leaks.
     */
    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "onDestroy called.");
        if (mediaPlayer != null) {
            // SharedPreferences are not cleared here. The last playback position is intentionally
            // persisted across app sessions (even if the app is fully closed and restarted).

            // If the MediaPlayer is playing, stop it before releasing resources.
            if (mediaPlayer.isPlaying()) {
                mediaPlayer.stop();
            }
            // Release the MediaPlayer resources. This is critical to free up system resources.
            mediaPlayer.release();
            // Set the MediaPlayer instance to null to help with garbage collection and prevent further use.
            mediaPlayer = null;
            Log.d(TAG, "MediaPlayer released.");
        }
    }
}
