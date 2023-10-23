use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use std::time::Duration;
use std::thread;

async fn index() -> impl Responder {
    thread::sleep(Duration::from_millis(200));
    HttpResponse::Ok().json("{\"Hello\": \"Actix\"}")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/actix", web::get().to(index))
    })
    .bind("0.0.0.0:8000")?
    .run()
    .await
}
