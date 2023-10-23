package main

import (
	"encoding/json"
	"net/http"
	"time"

	"github.com/go-chi/chi"
)

type Message struct {
	Hello string `json:"Hello"`
}

func main() {
	r := chi.NewRouter()
	r.Get("/chi", func(w http.ResponseWriter, r *http.Request) {
		time.Sleep(200 * time.Millisecond)
		message := Message{Hello: "Chi"}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(message)
	})
	http.ListenAndServe(":3000", r)
}
