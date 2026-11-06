# Range-Scalp Bot

*Updated Fri Nov 06 16:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49709 | 43330 | 6379 (76) | 2 | $-13963.89 | -4.5% |
| **+10¢** | 37106 | 29686 | 7420 (101) | 2 | $-12857.33 | -5.5% |
| **+15¢** | 31078 | 23084 | 7994 (130) | 2 | $-11751.73 | -6.0% |
| **+20¢** | 27627 | 19245 | 8382 (171) | 2 | $-10401.15 | -6.0% |
| **+10¢ (15¢ stop)** | 60571 | 60474 | 97 (57) | 0 | $-22410.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 16:11 | +10 stop | XRP | DOWN | 0.65 | 0.91 | 2.35 |
| 11-06 16:10 | +10 stop | XRP | UP | 0.64 | 0.46 | -2.15 |
| 11-06 16:10 | +10 | XRP | UP | 0.64 | open |  |
| 11-06 16:10 | +5 | XRP | UP | 0.64 | open |  |
| 11-06 16:08 | +10 | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 11-06 16:08 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-06 16:07 | +10 stop | XRP | DOWN | 0.46 | 0.24 | -2.51 |
| 11-06 16:05 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 16:05 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-06 16:05 | +10 stop | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 11-06 16:05 | +5 | XRP | UP | 0.65 | 0.75 | 0.72 |
| 11-06 16:04 | +5 | ZEC | UP | 0.58 | open |  |
| 11-06 16:04 | +10 stop | DOGE | DOWN | 0.51 | 0.67 | 1.26 |
| 11-06 16:04 | +5 | DOGE | DOWN | 0.51 | 0.56 | 0.14 |
| 11-06 16:04 | +10 stop | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 11-06 16:04 | +10 stop | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-06 16:04 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-06 16:03 | +10 stop | ZEC | UP | 0.55 | 0.40 | -1.85 |
| 11-06 16:03 | +10 | ZEC | UP | 0.55 | open |  |
| 11-06 16:03 | +5 | ZEC | UP | 0.55 | 0.63 | 0.45 |
| 11-06 16:03 | +5 | XRP | UP | 0.67 | 0.73 | 0.30 |
| 11-06 16:03 | +10 stop | DOGE | UP | 0.57 | 0.37 | -2.35 |
| 11-06 16:03 | +10 stop | ETH | UP | 0.59 | 0.41 | -2.14 |
| 11-06 16:02 | +10 stop | NEAR | UP | 0.60 | 0.43 | -2.05 |
| 11-06 16:02 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-06 16:02 | +10 stop | XRP | UP | 0.66 | 0.45 | -2.44 |
| 11-06 16:02 | +20 | XRP | UP | 0.67 | open |  |
| 11-06 16:02 | +15 | XRP | UP | 0.67 | open |  |
| 11-06 16:02 | +10 | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-06 16:02 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 11-06 16:01 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-06 16:01 | +20 | HYPE | DOWN | 0.69 | 0.90 | 1.91 |
| 11-06 16:01 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 16:01 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-06 16:01 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-06 16:01 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 11-06 16:01 | +20 | DOGE | DOWN | 0.56 | 0.79 | 2.00 |
| 11-06 16:01 | +15 | DOGE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-06 16:01 | +10 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-06 16:01 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
