# Range-Scalp Bot

*Updated Thu Nov 12 03:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56515 | 49270 | 7245 (98) | 7 | $-15538.10 | -4.4% |
| **+10¢** | 42234 | 33783 | 8451 (128) | 7 | $-14479.44 | -5.5% |
| **+15¢** | 35416 | 26313 | 9103 (162) | 6 | $-13145.24 | -5.9% |
| **+20¢** | 31552 | 22002 | 9550 (212) | 7 | $-11507.23 | -5.8% |
| **+10¢ (15¢ stop)** | 68903 | 68780 | 123 (73) | 0 | $-25448.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 03:11 | +10 stop | HYPE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-12 03:10 | +10 stop | NEAR | UP | 0.61 | 0.32 | -3.23 |
| 11-12 03:10 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-12 03:08 | +10 stop | HYPE | DOWN | 0.64 | 0.20 | -4.69 |
| 11-12 03:08 | +10 stop | NEAR | DOWN | 0.56 | 0.69 | 0.97 |
| 11-12 03:08 | +10 stop | ETH | DOWN | 0.56 | 0.69 | 0.97 |
| 11-12 03:08 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 11-12 03:08 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 11-12 03:08 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 11-12 03:07 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 11-12 03:06 | +10 stop | NEAR | DOWN | 0.65 | 0.46 | -2.24 |
| 11-12 03:06 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 11-12 03:06 | +10 stop | HYPE | DOWN | 0.65 | 0.49 | -1.94 |
| 11-12 03:06 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-12 03:06 | +15 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-12 03:06 | +10 | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-12 03:06 | +5 | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-12 03:05 | +10 stop | ETH | DOWN | 0.64 | 0.45 | -2.25 |
| 11-12 03:05 | +10 stop | BTC | UP | 0.51 | 0.70 | 1.57 |
| 11-12 03:05 | +10 | BTC | UP | 0.51 | 0.70 | 1.57 |
| 11-12 03:05 | +5 | BTC | UP | 0.51 | 0.59 | 0.45 |
| 11-12 03:05 | +10 stop | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 11-12 03:04 | +5 | SOL | UP | 0.64 | open |  |
| 11-12 03:03 | +10 | NEAR | UP | 0.68 | open |  |
| 11-12 03:03 | +5 | NEAR | UP | 0.69 | open |  |
| 11-12 03:03 | +5 | DOGE | UP | 0.71 | open |  |
| 11-12 03:03 | +10 stop | NEAR | UP | 0.71 | 0.53 | -2.13 |
| 11-12 03:03 | +10 stop | XRP | UP | 0.65 | 0.48 | -2.04 |
| 11-12 03:03 | +10 | XRP | UP | 0.65 | open |  |
| 11-12 03:02 | +5 | XRP | UP | 0.68 | open |  |
| 11-12 03:02 | +5 | BNB | UP | 0.68 | open |  |
| 11-12 03:02 | +10 stop | ZEC | UP | 0.65 | 0.49 | -1.94 |
| 11-12 03:02 | +20 | ZEC | UP | 0.66 | open |  |
| 11-12 03:02 | +15 | ZEC | UP | 0.66 | open |  |
| 11-12 03:02 | +10 | ZEC | UP | 0.65 | open |  |
| 11-12 03:02 | +5 | ZEC | UP | 0.65 | open |  |
| 11-12 03:02 | +10 stop | DOGE | UP | 0.67 | 0.50 | -2.04 |
| 11-12 03:02 | +20 | DOGE | UP | 0.67 | open |  |
| 11-12 03:02 | +15 | DOGE | UP | 0.67 | open |  |
| 11-12 03:02 | +10 | DOGE | UP | 0.67 | open |  |
