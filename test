package me.reminisce

import scala.util.Properties._

object ApplicationConfiguration {

  // Development ? Release ?
  val appMode = envOrElse("GAME_CREATOR_MODE", "DEV")

  val hostName = envOrElse("GAME_CREATOR_HOST", "localhost")
  val serverPort = envOrElse("GAME_CREATOR_PORT", "9900").toInt

  val mongoHost = envOrElse("MONGODB_HOST", hostName)
  val mongodbName = envOrElse("REMINISCE_MONGO_DB", "mydb")

}
