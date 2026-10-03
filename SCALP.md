# Range-Scalp Bot

*Updated Sat Oct 03 04:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 168 | 142 | 26 (1) | 1 | $-71.98 | -6.7% |
| **+10¢** | 141 | 115 | 26 (1) | 1 | $-30.81 | -3.4% |
| **+15¢** | 115 | 88 | 27 (1) | 0 | $-27.86 | -3.8% |
| **+20¢** | 321 | 227 | 94 (2) | 1 | $-91.81 | -4.6% |
| **+10¢ (15¢ stop)** | 234 | 234 | 0 (0) | 1 | $-108.16 | -7.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 04:16 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-03 04:16 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-03 04:16 | +5 | HYPE | DOWN | 0.61 | open |  |
| 10-03 04:16 | +10 stop | HYPE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-03 04:16 | +20 | HYPE | DOWN | 0.48 | open |  |
| 10-03 04:16 | +15 | HYPE | DOWN | 0.48 | 0.65 | 1.36 |
| 10-03 04:16 | +10 | HYPE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-03 04:16 | +5 | HYPE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-03 04:11 | +10 stop | BNB | DOWN | 0.71 | 0.18 | -5.56 |
| 10-03 04:11 | +15 | BNB | DOWN | 0.71 | yes | -7.25 |
| 10-03 04:11 | +10 | BNB | DOWN | 0.71 | yes | -7.25 |
| 10-03 04:11 | +5 | BNB | DOWN | 0.71 | yes | -7.25 |
| 10-03 04:09 | +10 stop | BNB | DOWN | 0.59 | 0.78 | 1.60 |
| 10-03 04:08 | +10 stop | BNB | UP | 0.64 | 0.42 | -2.54 |
| 10-03 04:08 | +10 stop | BTC | UP | 0.62 | 0.35 | -3.03 |
| 10-03 04:07 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-03 04:06 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.08 |
| 10-03 04:06 | +5 | SOL | UP | 0.66 | 0.83 | 1.44 |
| 10-03 04:06 | +10 stop | SOL | UP | 0.66 | 0.83 | 1.44 |
| 10-03 04:05 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 10-03 04:05 | +20 | BTC | UP | 0.69 | no | -7.05 |
| 10-03 04:05 | +15 | BTC | UP | 0.69 | no | -7.05 |
| 10-03 04:05 | +10 | BTC | UP | 0.69 | no | -7.05 |
| 10-03 04:05 | +5 | BTC | UP | 0.69 | no | -7.05 |
| 10-03 04:05 | +10 stop | ETH | UP | 0.70 | 0.53 | -2.03 |
| 10-03 04:05 | +10 stop | SOL | UP | 0.55 | 0.35 | -2.34 |
| 10-03 04:04 | +5 | XRP | UP | 0.66 | no | -6.75 |
| 10-03 04:04 | +10 stop | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-03 04:03 | +5 | XRP | UP | 0.59 | 0.67 | 0.47 |
| 10-03 04:03 | +10 stop | ZEC | DOWN | 0.71 | 0.54 | -2.02 |
| 10-03 04:03 | +10 stop | ETH | UP | 0.59 | 0.72 | 0.98 |
| 10-03 04:02 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-03 04:02 | +10 stop | ETH | DOWN | 0.59 | 0.40 | -2.24 |
| 10-03 04:02 | +20 | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 10-03 04:02 | +15 | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 10-03 04:02 | +10 | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-03 04:02 | +5 | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-03 04:02 | +10 stop | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 04:02 | +20 | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-03 04:02 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
