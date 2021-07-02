"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._now_playing = ()
        self._paused = 0

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")

        self._videos = self._video_library._videos

        for key in self._videos:
            tags = " ".join([tag for tag in self._videos[key]._tags])
            print(self._videos[key]._title + " (" + self._videos[key]._video_id + ") [" + tags + "]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        self._up_next = ()

        for k, v in self._video_library._videos.items():
            if k == video_id:
                self._up_next = k, v
                break
            else:
                continue

        if not(self._up_next):
            print("Cannot play video: Video does not exist")

        else:
            if self._now_playing:
                print("Stopping video: " + self._now_playing[1].title)

            self._now_playing = self._up_next
            print("Playing video: " + self._now_playing[1].title)
            self._paused = 0

    def stop_video(self):
        """Stops the current video."""

        if self._now_playing:
            print("Stopping video: " + self._now_playing[1].title)
            self._now_playing = ()
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        if not (self._video_library._videos):
            print("No videos available")
        else:
            self._videos_list = [(k, v) for k, v in self._video_library._videos.items()]
            x = random.randint(0, len(self._videos_list)-1)
            self.play_video(self._videos_list[x][0])

    def pause_video(self):
        """Pauses the current video."""

        if self._now_playing:
            if self._paused == 1:
                print("Video already paused: " + self._now_playing[1].title)
            else:
                print("Pausing video: " + self._now_playing[1].title)
                self._paused = 1
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._now_playing:
            if self._paused == 0:
                print("Cannot continue video: Video is not paused")
            else:
                print("Continuing video: " + self._now_playing[1].title)
                self._paused = 0
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self._now_playing:
            tags = " ".join([tag for tag in self._now_playing[1].tags])
            if self._paused:
                print("Currently playing: " + self._now_playing[1].title + " (" + self._now_playing[1]._video_id +
                      ") [" + tags + "] - PAUSED")
            else:
                print("Currently playing: " + self._now_playing[1].title + " (" + self._now_playing[1]._video_id +
                      ") [" + tags + "]")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
