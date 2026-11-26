# Range-Scalp Bot

*Updated Thu Nov 26 10:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72522 | 63311 | 9211 (158) | 4 | $-19226.17 | -4.2% |
| **+10¢** | 54085 | 43329 | 10756 (203) | 4 | $-17803.00 | -5.2% |
| **+15¢** | 45291 | 33705 | 11586 (261) | 4 | $-15877.60 | -5.6% |
| **+20¢** | 40315 | 28113 | 12202 (327) | 4 | $-14271.53 | -5.6% |
| **+10¢ (15¢ stop)** | 88303 | 88094 | 209 (128) | 0 | $-32403.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 10:37 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 11-26 10:37 | +10 stop | DOGE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-26 10:37 | +5 | DOGE | DOWN | 0.65 | 0.80 | 1.23 |
| 11-26 10:36 | +10 stop | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 11-26 10:36 | +15 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 11-26 10:36 | +10 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 11-26 10:36 | +5 | XRP | DOWN | 0.58 | 0.67 | 0.56 |
| 11-26 10:33 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-26 10:33 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-26 10:33 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-26 10:33 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-26 10:33 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-26 10:33 | +10 stop | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 11-26 10:33 | +10 stop | ETH | DOWN | 0.56 | 0.68 | 0.86 |
| 11-26 10:33 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-26 10:32 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-26 10:32 | +20 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 10:32 | +15 | XRP | DOWN | 0.59 | 0.75 | 1.29 |
| 11-26 10:32 | +10 | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-26 10:32 | +5 | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-26 10:32 | +10 stop | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 11-26 10:32 | +20 | BNB | DOWN | 0.63 | 0.83 | 1.73 |
| 11-26 10:32 | +15 | BNB | DOWN | 0.63 | 0.80 | 1.41 |
| 11-26 10:32 | +10 | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 11-26 10:32 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 11-26 10:31 | +10 stop | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-26 10:31 | +20 | HYPE | DOWN | 0.57 | 0.79 | 1.90 |
| 11-26 10:31 | +15 | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-26 10:31 | +10 | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-26 10:31 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-26 10:31 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.96 |
| 11-26 10:31 | +20 | SOL | UP | 0.63 | open |  |
| 11-26 10:31 | +15 | SOL | UP | 0.63 | open |  |
| 11-26 10:31 | +10 | SOL | UP | 0.63 | open |  |
| 11-26 10:31 | +5 | SOL | UP | 0.63 | open |  |
| 11-26 10:31 | +10 stop | BTC | UP | 0.64 | 0.48 | -1.95 |
| 11-26 10:31 | +20 | BTC | UP | 0.64 | open |  |
| 11-26 10:31 | +15 | BTC | UP | 0.64 | open |  |
| 11-26 10:31 | +10 | BTC | UP | 0.63 | open |  |
| 11-26 10:31 | +5 | BTC | UP | 0.62 | open |  |
