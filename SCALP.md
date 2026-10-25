# Range-Scalp Bot

*Updated Sun Oct 25 14:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33274 | 29036 | 4238 (42) | 1 | $-9314.36 | -4.4% |
| **+10¢** | 24906 | 20000 | 4906 (60) | 1 | $-8277.34 | -5.3% |
| **+15¢** | 20838 | 15554 | 5284 (83) | 1 | $-7465.63 | -5.7% |
| **+20¢** | 18463 | 12929 | 5534 (105) | 0 | $-6589.70 | -5.7% |
| **+10¢ (15¢ stop)** | 40808 | 40748 | 60 (32) | 0 | $-15595.70 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 14:23 | +5 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-25 14:22 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-25 14:22 | +10 stop | HYPE | DOWN | 0.56 | 0.69 | 0.97 |
| 10-25 14:21 | +10 stop | HYPE | UP | 0.63 | 0.40 | -2.64 |
| 10-25 14:21 | +15 | HYPE | UP | 0.63 | open |  |
| 10-25 14:21 | +10 | HYPE | UP | 0.63 | open |  |
| 10-25 14:21 | +5 | HYPE | UP | 0.63 | open |  |
| 10-25 14:21 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-25 14:21 | +15 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 10-25 14:21 | +10 | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-25 14:21 | +5 | BNB | DOWN | 0.59 | 0.68 | 0.57 |
| 10-25 14:18 | +10 stop | ZEC | DOWN | 0.61 | 0.45 | -1.95 |
| 10-25 14:18 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-25 14:18 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-25 14:17 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 14:17 | +20 | SOL | DOWN | 0.65 | 0.85 | 1.75 |
| 10-25 14:17 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-25 14:17 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 14:17 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-25 14:16 | +10 stop | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-25 14:16 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.92 |
| 10-25 14:16 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 14:16 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-25 14:16 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-25 14:16 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-25 14:16 | +20 | ETH | DOWN | 0.69 | 0.90 | 1.89 |
| 10-25 14:16 | +15 | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 10-25 14:16 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-25 14:16 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 10-25 14:16 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-25 14:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-25 14:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-25 14:16 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-25 14:16 | +5 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-25 14:16 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-25 14:16 | +20 | HYPE | DOWN | 0.68 | 0.90 | 1.97 |
| 10-25 14:16 | +15 | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-25 14:16 | +10 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-25 14:16 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 10-25 14:16 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.86 |
