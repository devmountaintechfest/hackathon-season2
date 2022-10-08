package xml_test

import (
	"testing"

	"github.com/markkj/hackathon-season2/internal/xml"
)

func BenchmarkReadXMLFromHackathon(b *testing.B) {
	for n := 0; n < b.N; n++ {
		xml.ReadXMLFromHackathon("../../data-devclub-1.xml")
	}
}
