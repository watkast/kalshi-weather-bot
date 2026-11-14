# Range-Scalp Bot

*Updated Sat Nov 14 10:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59362 | 51802 | 7560 (107) | 0 | $-15986.51 | -4.3% |
| **+10¢** | 44337 | 35487 | 8850 (142) | 0 | $-15004.49 | -5.4% |
| **+15¢** | 37155 | 27611 | 9544 (178) | 0 | $-13638.88 | -5.9% |
| **+20¢** | 33099 | 23082 | 10017 (230) | 1 | $-12007.73 | -5.8% |
| **+10¢ (15¢ stop)** | 72209 | 72067 | 142 (82) | 0 | $-26535.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 10:53 | +5 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-14 10:53 | +10 stop | BTC | DOWN | 0.62 | 0.47 | -1.85 |
| 11-14 10:53 | +10 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-14 10:53 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-14 10:52 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-14 10:52 | +20 | SOL | DOWN | 0.71 | 0.98 | 2.49 |
| 11-14 10:52 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 11-14 10:52 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-14 10:52 | +5 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-14 10:49 | +10 stop | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 11-14 10:49 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 11-14 10:49 | +15 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-14 10:49 | +10 | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 11-14 10:49 | +5 | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 11-14 10:49 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-14 10:49 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-14 10:49 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-14 10:48 | +10 stop | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-14 10:48 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-14 10:48 | +5 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-14 10:45 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 10:45 | +20 | ZEC | DOWN | 0.70 | 0.92 | 1.97 |
| 11-14 10:45 | +15 | ZEC | DOWN | 0.70 | 0.92 | 1.97 |
| 11-14 10:45 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 10:45 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-14 10:45 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-14 10:45 | +20 | DOGE | DOWN | 0.69 | 0.91 | 1.98 |
| 11-14 10:45 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-14 10:45 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-14 10:45 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-14 10:45 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 10:45 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-14 10:45 | +15 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 11-14 10:45 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 10:45 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 11-14 10:40 | +10 stop | HYPE | DOWN | 0.64 | 0.45 | -2.25 |
| 11-14 10:40 | +20 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-14 10:40 | +15 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-14 10:40 | +10 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-14 10:40 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
