# Range-Scalp Bot

*Updated Thu Nov 05 06:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48111 | 41900 | 6211 (73) | 0 | $-13841.01 | -4.6% |
| **+10¢** | 35941 | 28724 | 7217 (99) | 0 | $-12712.47 | -5.6% |
| **+15¢** | 30118 | 22349 | 7769 (127) | 0 | $-11611.16 | -6.1% |
| **+20¢** | 26756 | 18618 | 8138 (166) | 0 | $-10268.21 | -6.1% |
| **+10¢ (15¢ stop)** | 58636 | 58543 | 93 (56) | 0 | $-21770.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 05:51 | +10 stop | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-05 05:51 | +10 | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-05 05:51 | +5 | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-05 05:49 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 05:49 | +10 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 05:49 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-05 05:46 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-05 05:46 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.93 |
| 11-05 05:46 | +15 | BTC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-05 05:46 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-05 05:46 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-05 05:45 | +10 stop | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-05 05:45 | +20 | HYPE | DOWN | 0.58 | 0.79 | 1.80 |
| 11-05 05:45 | +15 | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
| 11-05 05:45 | +10 | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-05 05:45 | +5 | HYPE | DOWN | 0.58 | 0.65 | 0.36 |
| 11-05 05:43 | +10 stop | BTC | UP | 0.28 | 0.54 | 2.27 |
| 11-05 05:42 | +10 stop | XRP | UP | 0.59 | 0.33 | -2.93 |
| 11-05 05:42 | +20 | XRP | UP | 0.59 | no | -6.07 |
| 11-05 05:42 | +15 | XRP | UP | 0.59 | no | -6.07 |
| 11-05 05:42 | +10 | XRP | UP | 0.60 | no | -6.14 |
| 11-05 05:42 | +5 | XRP | UP | 0.60 | no | -6.14 |
| 11-05 05:41 | +10 stop | ETH | UP | 0.63 | 0.45 | -2.15 |
| 11-05 05:37 | +10 stop | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-05 05:37 | +10 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-05 05:37 | +5 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-05 05:37 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 11-05 05:37 | +5 | HYPE | UP | 0.59 | 0.66 | 0.41 |
| 11-05 05:36 | +20 | ZEC | UP | 0.71 | 0.91 | 1.79 |
| 11-05 05:36 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 11-05 05:36 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 11-05 05:35 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-05 05:35 | +15 | HYPE | UP | 0.56 | 0.72 | 1.31 |
| 11-05 05:35 | +10 | HYPE | UP | 0.55 | 0.66 | 0.76 |
| 11-05 05:35 | +5 | HYPE | UP | 0.55 | 0.60 | 0.15 |
| 11-05 05:34 | +10 stop | ETH | UP | 0.68 | 0.81 | 0.99 |
| 11-05 05:34 | +10 stop | BNB | UP | 0.67 | 0.52 | -1.84 |
| 11-05 05:34 | +15 | SOL | UP | 0.68 | 0.88 | 1.78 |
| 11-05 05:34 | +10 stop | BTC | UP | 0.55 | 0.73 | 1.48 |
| 11-05 05:34 | +10 stop | SOL | UP | 0.68 | 0.82 | 1.15 |
