1. ["If you target Android 8.0 (API level 26) and post a notification without specifying a notification channel, the notification does not appear and the system logs an error."](https://developer.android.com/training/notify-user/channels)
1. `minSdkVersion=x` prevents the APK from being installed on anything less than. `targetSdkVersion=x` disables extra compatibility code that is run to keep the APK compatible with version x.
1. Android Studio 0.80 beta is, by default, [broken](http://stackoverflow.com/questions/24465289/android-studio-failure-install-failed-older-sdk).
1. Handling menu clicks is as stupid as you want it to be, but [here is a simpler one](http://stackoverflow.com/a/7480103/1558430)
1. For whatever reason, [it is impossible to set a negative value on a NumberPicker](http://stackoverflow.com/questions/20968561/android-numberpicker-negative-values). You can only subtract the value by a negative number after the fact.
1. Do know what these mean: activity/fragment lifecycles, device rotation, services, broadcasts, background tasks, asynchronous tasks, views, adapters, recyclerview, "view holder pattern"
1. Strings are put inside `project_root/app/src/main/res/values/strings.xml`, because nested folders are the best.
1. [The plus thing in the XML](http://developer.android.com/training/basics/firstapp/building-ui.html), like `android:id="@+id/edit_message"`, is required only for the line that defines it.
1. `android:hint` are placeholder texts.
1. [`layout_weight` is a relative number](http://stackoverflow.com/questions/3995825/what-does-androidlayout-weight-mean). A `layout_weight` of 1 means 100% of the width *IF* the control happens to be the only control inside a `LinearView` with the weight specified. If two controls have the weight specified (say 1, 1), then each control shares 50% of the width.
1. If `layout_weight` is given, [then](http://developer.android.com/training/basics/firstapp/building-ui.html) `layout_width` is useless (irrelevant), and should be set to 0dp or 0px.
1. The back button does ["back navigation"](http://developer.android.com/design/patterns/navigation.html) (whichever activity shown in reverse chronological order); the in-app backs do "up navigation". The term "up" refers to the hierarchical parent of the current activity, a hierarchy you declare in `AndroidManifest.xml`.
1. Putting a library into `libs/` seems to do it.
1. There are project (`./build.gradle`) and app-level (`./app/build.gradle`) gradle files. The former defines dependencies, and the latter uses them.
1. If gradle is too old, update the `classpath 'com.android.tools.build:gradle:2.1.2'`... in the gradle file. Gradle will update itself. [True fact.](http://stackoverflow.com/questions/17634708/android-studio-upgraded-from-0-1-9-to-0-2-0-causing-gradle-build-errors-now/17648742#17648742)
1. Order in the layout xml files matters.
1. The project's JDK settings is in File > Project Structure, which is not in Settings for studio.
1. If you don't know what fresh hell you are doing, [here is a layouts cheat sheet](http://labs.udacity.com/images/Layout-Cheat-Sheet.pdf).
1. Accessing the Internet on the main thread, get this, raises the `NetworkOnMainThreadException`.
1. [AsyncTask](http://stackoverflow.com/questions/3921816/can-i-pass-different-types-of-parameters-to-an-asynctask-in-android) takes just one type of parameter, but you can use "the setter" (?) to use additional types, or simply [pass in an `Object`](http://stackoverflow.com/a/9077177) and re-cast from there.
1. ["The difference between Handler and AsyncTask is: Use AsyncTask when Caller thread is a UI Thread."](http://stackoverflow.com/a/9800870)
1. It is near impossible to [conjure a popup from a non-activity class](http://stackoverflow.com/a/31221646).
1. `(an AsyncTask).get()` [immediately gets the value from its execute()](http://stackoverflow.com/a/10972142). Then again, that is a synchronous move.
1. Activity [apparently](http://stackoverflow.com/a/9192916/1558430) extends Context.
1. Find your dependency versions on [this website](http://search.maven.org/#search%7Cga%7C1%7Cio.reactivex.rxjava). It only searches on mavenCentral, I think.
1. [Two-way binding is **not** natively supported](https://medium.com/@fabioCollini/android-data-binding-f9f9d3afc761#.pfcgcnfo5) by the designer thing, but there are lots of [one-way binding libraries](https://developer.android.com/topic/libraries/data-binding/index.html) available.
1. To use that `com.android.databinding` plugin, the layout file must have `<Layout>` as the root, not anything else, like `<LinearLayout>`.
1. [Java 8 must be explicitly enabled](http://stackoverflow.com/a/37004259/1558430)
1. The superclass of your activity has a [`setTitle()`](http://stackoverflow.com/questions/3975550/android-how-to-change-the-application-title) that does what you think it does.
1. [Loser answered the wrong base64 question](http://stackoverflow.com/a/29383697/1558430), but it works. [This should work.](http://stackoverflow.com/a/15683305/1558430)
1. Two apps signed with the same key can [securely share code and data](https://developer.android.com/studio/publish/app-signing.html#considerations).
1. adbd cannot run as root in production builds.
1. The default support library already supports [automatic day/night theming](https://android-developers.googleblog.com/2016/02/android-support-library-232.html). You just need to specify `AppCompatDelegate.MODE_NIGHT_AUTO` and it will be themed for you.
1. Burak says [`Serializable` is a form of reflection, and has poor performance.](https://android.jlelse.eu/yet-another-awesome-kotlin-feature-parcelize-5439718ba220)
1. In some cases, [`onDestroy` is never called when an activity is destroyed.](https://academy.realm.io/posts/sf-fabien-davos-modern-android-ditching-activities-fragments/)
1. Sometimes you might want to check if you can run code based on the SDK version with which your app is built (like `Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR2`). Actually, I don't think you'll ever need to do that.
1. [try-with-resources is only supported if your minSdkVersion is set to 19 or higher.](https://stackoverflow.com/a/24290875/1558430) It looks like `try (foo = new SomeResourceLikeAFile()) { foo... }`. Multiple resources can be tried by separating with a `;`.
1. `startActivity` accepts an `Intent` rather than `Activity` because reasons.
1. If even one of your neurons fire up, you would have noticed that `new Intent(CurrentActivity.this, ...)` and `new Intent(this, ...)` are identical statements.
1. IDs are under_scored. Variables are camelCased, As always, because reasons.
1. It is possible to name your package using someone else's domain, like `com.microsoft.lol`.
1. "Target SDK version" is the level at which you can use the SDK's features. ["Min SDK version"][stackoverflow 14] is the level at which you, the developer, have made sure the app still works by handling missing features properly.
1. The API level of a [pre-release](https://developer.android.com/studio/releases/platforms#P_preview) version of Android is not a number. For P preview, the API level is just "P".