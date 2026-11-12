# Range-Scalp Bot

*Updated Thu Nov 12 04:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56634 | 49369 | 7265 (98) | 1 | $-15619.15 | -4.4% |
| **+10¢** | 42320 | 33846 | 8474 (128) | 2 | $-14565.62 | -5.5% |
| **+15¢** | 35480 | 26357 | 9123 (162) | 3 | $-13203.13 | -5.9% |
| **+20¢** | 31610 | 22036 | 9574 (212) | 4 | $-11594.10 | -5.8% |
| **+10¢ (15¢ stop)** | 69041 | 68918 | 123 (73) | 1 | $-25494.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 04:23 | +10 stop | NEAR | DOWN | 0.55 | 0.70 | 1.17 |
| 11-12 04:23 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 04:23 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-12 04:23 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 04:23 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 11-12 04:23 | +10 stop | HYPE | DOWN | 0.54 | 0.75 | 1.78 |
| 11-12 04:23 | +5 | HYPE | DOWN | 0.54 | 0.61 | 0.35 |
| 11-12 04:22 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 11-12 04:22 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-12 04:22 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-12 04:22 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-12 04:22 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 11-12 04:21 | +10 stop | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-12 04:21 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-12 04:21 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-12 04:20 | +5 | NEAR | UP | 0.62 | open |  |
| 11-12 04:20 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 11-12 04:20 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 04:20 | +5 | DOGE | DOWN | 0.65 | 0.74 | 0.60 |
| 11-12 04:19 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 04:19 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 04:19 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 11-12 04:19 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.72 |
| 11-12 04:19 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-12 04:19 | +5 | DOGE | DOWN | 0.60 | 0.69 | 0.58 |
| 11-12 04:19 | +10 stop | SOL | DOWN | 0.55 | 0.68 | 0.96 |
| 11-12 04:19 | +5 | SOL | DOWN | 0.55 | 0.60 | 0.15 |
| 11-12 04:17 | +10 stop | HYPE | UP | 0.57 | 0.38 | -2.25 |
| 11-12 04:17 | +10 stop | BNB | UP | 0.56 | 0.39 | -2.05 |
| 11-12 04:17 | +10 stop | NEAR | UP | 0.64 | 0.39 | -2.84 |
| 11-12 04:17 | +20 | NEAR | UP | 0.64 | open |  |
| 11-12 04:17 | +15 | NEAR | UP | 0.64 | open |  |
| 11-12 04:17 | +10 | NEAR | UP | 0.64 | open |  |
| 11-12 04:17 | +5 | NEAR | UP | 0.65 | 0.71 | 0.29 |
| 11-12 04:17 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 11-12 04:17 | +5 | SOL | DOWN | 0.47 | 0.60 | 0.95 |
| 11-12 04:16 | +10 stop | BNB | DOWN | 0.60 | 0.44 | -1.95 |
| 11-12 04:16 | +10 | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 11-12 04:16 | +5 | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 11-12 04:16 | +10 stop | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
