# Range-Scalp Bot

*Updated Sun Oct 25 04:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32566 | 28396 | 4170 (42) | 5 | $-9280.25 | -4.5% |
| **+10¢** | 24375 | 19546 | 4829 (60) | 6 | $-8312.51 | -5.4% |
| **+15¢** | 20407 | 15212 | 5195 (83) | 6 | $-7462.97 | -5.8% |
| **+20¢** | 18076 | 12639 | 5437 (105) | 7 | $-6611.35 | -5.8% |
| **+10¢ (15¢ stop)** | 40014 | 39954 | 60 (32) | 0 | $-15288.11 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 04:23 | +10 stop | NEAR | UP | 0.61 | 0.45 | -1.95 |
| 10-25 04:23 | +10 stop | BNB | DOWN | 0.68 | 0.44 | -2.74 |
| 10-25 04:23 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-25 04:23 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-25 04:23 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-25 04:23 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-25 04:23 | +10 stop | XRP | UP | 0.70 | 0.52 | -2.13 |
| 10-25 04:23 | +5 | XRP | UP | 0.70 | open |  |
| 10-25 04:22 | +10 stop | SOL | UP | 0.60 | 0.43 | -2.05 |
| 10-25 04:21 | +5 | SOL | UP | 0.62 | open |  |
| 10-25 04:21 | +10 stop | NEAR | UP | 0.71 | 0.56 | -1.83 |
| 10-25 04:21 | +10 stop | ETH | UP | 0.61 | 0.78 | 1.40 |
| 10-25 04:20 | +10 stop | SOL | DOWN | 0.54 | 0.38 | -1.95 |
| 10-25 04:20 | +15 | SOL | DOWN | 0.54 | open |  |
| 10-25 04:20 | +5 | SOL | DOWN | 0.54 | 0.63 | 0.55 |
| 10-25 04:20 | +10 stop | BTC | UP | 0.61 | 0.75 | 1.09 |
| 10-25 04:20 | +20 | BTC | UP | 0.61 | 0.82 | 1.82 |
| 10-25 04:20 | +15 | BTC | UP | 0.61 | 0.76 | 1.20 |
| 10-25 04:20 | +10 | BTC | UP | 0.61 | 0.75 | 1.09 |
| 10-25 04:20 | +5 | BTC | UP | 0.63 | 0.75 | 0.89 |
| 10-25 04:20 | +5 | XRP | DOWN | 0.56 | 0.62 | 0.30 |
| 10-25 04:18 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-25 04:17 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-25 04:16 | +10 stop | XRP | DOWN | 0.65 | 0.25 | -4.30 |
| 10-25 04:16 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-25 04:16 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-25 04:16 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-25 04:16 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-25 04:16 | +10 stop | HYPE | UP | 0.54 | 0.75 | 1.74 |
| 10-25 04:16 | +20 | HYPE | UP | 0.54 | 0.75 | 1.74 |
| 10-25 04:16 | +15 | HYPE | UP | 0.54 | 0.75 | 1.78 |
| 10-25 04:16 | +10 | HYPE | UP | 0.54 | 0.75 | 1.78 |
| 10-25 04:16 | +5 | HYPE | UP | 0.54 | 0.59 | 0.15 |
| 10-25 04:16 | +5 | ETH | DOWN | 0.56 | 0.62 | 0.25 |
| 10-25 04:15 | +10 stop | ZEC | DOWN | 0.56 | 0.24 | -3.51 |
| 10-25 04:15 | +20 | ZEC | DOWN | 0.56 | open |  |
| 10-25 04:15 | +15 | ZEC | DOWN | 0.56 | open |  |
| 10-25 04:15 | +10 | ZEC | DOWN | 0.56 | open |  |
| 10-25 04:15 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
| 10-25 04:15 | +10 stop | NEAR | DOWN | 0.59 | 0.33 | -2.93 |
