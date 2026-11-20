# Range-Scalp Bot

*Updated Fri Nov 20 08:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66119 | 57707 | 8412 (125) | 3 | $-17782.25 | -4.3% |
| **+10¢** | 49371 | 39531 | 9840 (167) | 2 | $-16585.43 | -5.3% |
| **+15¢** | 41408 | 30794 | 10614 (214) | 2 | $-14942.13 | -5.8% |
| **+20¢** | 36863 | 25715 | 11148 (270) | 3 | $-13251.18 | -5.7% |
| **+10¢ (15¢ stop)** | 80527 | 80363 | 164 (98) | 0 | $-29714.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 08:28 | +10 stop | ZEC | UP | 0.67 | 0.41 | -2.93 |
| 11-20 08:26 | +10 stop | ETH | DOWN | 0.53 | 0.38 | -1.85 |
| 11-20 08:26 | +10 stop | NEAR | UP | 0.62 | 0.85 | 2.03 |
| 11-20 08:26 | +15 | NEAR | UP | 0.62 | 0.85 | 2.04 |
| 11-20 08:26 | +10 | NEAR | UP | 0.62 | 0.85 | 2.04 |
| 11-20 08:26 | +5 | NEAR | UP | 0.62 | 0.69 | 0.38 |
| 11-20 08:26 | +10 stop | SOL | UP | 0.68 | 0.79 | 0.82 |
| 11-20 08:26 | +5 | SOL | UP | 0.68 | 0.77 | 0.61 |
| 11-20 08:25 | +10 stop | DOGE | UP | 0.59 | 0.78 | 1.60 |
| 11-20 08:25 | +10 stop | ETH | DOWN | 0.68 | 0.45 | -2.64 |
| 11-20 08:25 | +5 | ETH | DOWN | 0.69 | open |  |
| 11-20 08:25 | +5 | SOL | DOWN | 0.47 | 0.65 | 1.46 |
| 11-20 08:24 | +10 stop | XRP | DOWN | 0.49 | 0.19 | -3.29 |
| 11-20 08:24 | +5 | XRP | DOWN | 0.49 | open |  |
| 11-20 08:24 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.85 |
| 11-20 08:24 | +15 | SOL | DOWN | 0.60 | open |  |
| 11-20 08:24 | +10 stop | DOGE | DOWN | 0.63 | 0.46 | -2.05 |
| 11-20 08:24 | +10 stop | BNB | UP | 0.51 | 0.66 | 1.16 |
| 11-20 08:24 | +10 stop | NEAR | UP | 0.29 | 0.53 | 2.07 |
| 11-20 08:24 | +10 stop | DOGE | UP | 0.41 | 0.52 | 0.75 |
| 11-20 08:23 | +5 | XRP | UP | 0.56 | 0.68 | 0.86 |
| 11-20 08:23 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 11-20 08:23 | +10 stop | SOL | DOWN | 0.52 | 0.63 | 0.75 |
| 11-20 08:23 | +10 stop | HYPE | UP | 0.67 | 0.85 | 1.58 |
| 11-20 08:23 | +5 | HYPE | UP | 0.67 | 0.74 | 0.43 |
| 11-20 08:23 | +10 stop | NEAR | DOWN | 0.59 | 0.43 | -1.95 |
| 11-20 08:22 | +10 stop | XRP | UP | 0.66 | 0.47 | -2.24 |
| 11-20 08:22 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 11-20 08:22 | +10 stop | BTC | UP | 0.67 | 0.43 | -2.74 |
| 11-20 08:22 | +10 stop | DOGE | UP | 0.59 | 0.44 | -1.85 |
| 11-20 08:22 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 11-20 08:21 | +10 stop | ZEC | UP | 0.69 | 0.49 | -2.33 |
| 11-20 08:21 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 11-20 08:21 | +10 stop | HYPE | UP | 0.54 | 0.67 | 0.96 |
| 11-20 08:21 | +10 stop | SOL | UP | 0.60 | 0.43 | -2.05 |
| 11-20 08:21 | +10 stop | ETH | DOWN | 0.58 | 0.77 | 1.59 |
| 11-20 08:21 | +5 | ETH | DOWN | 0.58 | 0.67 | 0.56 |
| 11-20 08:20 | +10 stop | NEAR | DOWN | 0.62 | 0.42 | -2.35 |
| 11-20 08:20 | +10 | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 11-20 08:20 | +5 | NEAR | DOWN | 0.62 | 0.71 | 0.58 |
