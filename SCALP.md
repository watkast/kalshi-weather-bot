# Range-Scalp Bot

*Updated Sat Nov 14 18:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59681 | 52074 | 7607 (107) | 0 | $-16134.27 | -4.3% |
| **+10¢** | 44584 | 35677 | 8907 (143) | 0 | $-15155.26 | -5.4% |
| **+15¢** | 37359 | 27755 | 9604 (180) | 0 | $-13774.08 | -5.9% |
| **+20¢** | 33279 | 23200 | 10079 (232) | 0 | $-12134.99 | -5.8% |
| **+10¢ (15¢ stop)** | 72620 | 72477 | 143 (82) | 0 | $-26692.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 18:25 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-14 18:25 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 11-14 18:25 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 18:25 | +10 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 18:25 | +5 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 18:24 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-14 18:24 | +20 | HYPE | DOWN | 0.63 | 0.93 | 2.76 |
| 11-14 18:24 | +15 | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-14 18:24 | +10 | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-14 18:24 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-14 18:17 | +10 | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-14 18:17 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 11-14 18:17 | +10 stop | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-14 18:16 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-14 18:16 | +20 | HYPE | DOWN | 0.63 | 0.83 | 1.73 |
| 11-14 18:16 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-14 18:16 | +10 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-14 18:16 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-14 18:16 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-14 18:16 | +20 | BTC | DOWN | 0.69 | 0.93 | 2.18 |
| 11-14 18:16 | +15 | BTC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-14 18:16 | +10 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-14 18:16 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-14 18:16 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-14 18:16 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-14 18:16 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-14 18:16 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-14 18:16 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 11-14 18:16 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-14 18:16 | +20 | ETH | DOWN | 0.65 | 0.86 | 1.85 |
| 11-14 18:16 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 11-14 18:16 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-14 18:16 | +5 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-14 18:11 | +5 | XRP | DOWN | 0.60 | 0.79 | 1.61 |
| 11-14 18:11 | +10 stop | BNB | UP | 0.69 | 0.82 | 1.04 |
| 11-14 18:11 | +15 | BNB | UP | 0.69 | 0.91 | 1.93 |
| 11-14 18:11 | +10 | BNB | UP | 0.69 | 0.82 | 1.04 |
| 11-14 18:11 | +5 | BNB | UP | 0.69 | 0.82 | 1.04 |
| 11-14 18:11 | +10 stop | XRP | UP | 0.37 | 0.20 | -1.97 |
| 11-14 18:11 | +5 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
