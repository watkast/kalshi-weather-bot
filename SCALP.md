# Range-Scalp Bot

*Updated Tue Nov 17 04:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62568 | 54585 | 7983 (117) | 8 | $-16954.41 | -4.3% |
| **+10¢** | 46729 | 37388 | 9341 (159) | 8 | $-15822.21 | -5.4% |
| **+15¢** | 39166 | 29091 | 10075 (201) | 8 | $-14369.40 | -5.8% |
| **+20¢** | 34910 | 24345 | 10565 (256) | 8 | $-12535.97 | -5.7% |
| **+10¢ (15¢ stop)** | 76162 | 76006 | 156 (92) | 0 | $-28062.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 04:40 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 11-17 04:39 | +10 stop | BNB | UP | 0.63 | 0.78 | 1.20 |
| 11-17 04:39 | +20 | BNB | UP | 0.63 | 0.85 | 1.94 |
| 11-17 04:39 | +15 | BNB | UP | 0.64 | 0.85 | 1.84 |
| 11-17 04:39 | +10 | BNB | UP | 0.64 | 0.78 | 1.10 |
| 11-17 04:39 | +5 | BNB | UP | 0.65 | 0.71 | 0.29 |
| 11-17 04:38 | +10 stop | DOGE | DOWN | 0.37 | 0.52 | 1.15 |
| 11-17 04:37 | +10 stop | ZEC | UP | 0.67 | 0.81 | 1.09 |
| 11-17 04:37 | +5 | BTC | DOWN | 0.59 | open |  |
| 11-17 04:36 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.03 |
| 11-17 04:36 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-17 04:36 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-17 04:36 | +10 | SOL | DOWN | 0.70 | open |  |
| 11-17 04:36 | +5 | SOL | DOWN | 0.70 | open |  |
| 11-17 04:36 | +10 stop | HYPE | DOWN | 0.62 | 0.28 | -3.72 |
| 11-17 04:36 | +15 | HYPE | DOWN | 0.62 | open |  |
| 11-17 04:36 | +10 | HYPE | DOWN | 0.62 | open |  |
| 11-17 04:36 | +5 | HYPE | DOWN | 0.60 | open |  |
| 11-17 04:36 | +10 stop | XRP | DOWN | 0.54 | 0.31 | -2.63 |
| 11-17 04:36 | +10 stop | BTC | DOWN | 0.64 | 0.34 | -3.33 |
| 11-17 04:35 | +10 stop | ETH | UP | 0.62 | 0.73 | 0.79 |
| 11-17 04:35 | +10 stop | ZEC | DOWN | 0.64 | 0.48 | -1.95 |
| 11-17 04:35 | +20 | ZEC | DOWN | 0.64 | open |  |
| 11-17 04:35 | +15 | ZEC | DOWN | 0.64 | open |  |
| 11-17 04:35 | +10 | ZEC | DOWN | 0.64 | open |  |
| 11-17 04:35 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-17 04:35 | +10 stop | DOGE | UP | 0.47 | 0.63 | 1.29 |
| 11-17 04:35 | +10 stop | XRP | UP | 0.42 | 0.54 | 0.84 |
| 11-17 04:34 | +5 | DOGE | DOWN | 0.57 | open |  |
| 11-17 04:34 | +10 stop | XRP | DOWN | 0.58 | 0.33 | -2.84 |
| 11-17 04:34 | +10 | XRP | DOWN | 0.58 | open |  |
| 11-17 04:34 | +5 | XRP | DOWN | 0.58 | open |  |
| 11-17 04:34 | +5 | NEAR | DOWN | 0.53 | open |  |
| 11-17 04:34 | +10 stop | BTC | DOWN | 0.60 | 0.40 | -2.34 |
| 11-17 04:34 | +10 | BTC | DOWN | 0.59 | open |  |
| 11-17 04:34 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-17 04:34 | +10 stop | DOGE | DOWN | 0.64 | 0.33 | -3.43 |
| 11-17 04:34 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-17 04:34 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-17 04:34 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.54 |
