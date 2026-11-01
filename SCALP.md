# Range-Scalp Bot

*Updated Sun Nov 01 15:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43629 | 38019 | 5610 (64) | 6 | $-12434.57 | -4.5% |
| **+10¢** | 32554 | 26076 | 6478 (85) | 6 | $-11139.94 | -5.4% |
| **+15¢** | 27246 | 20269 | 6977 (112) | 7 | $-10171.54 | -5.9% |
| **+20¢** | 24195 | 16886 | 7309 (146) | 6 | $-8979.44 | -5.9% |
| **+10¢ (15¢ stop)** | 53238 | 53152 | 86 (51) | 0 | $-20110.06 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 15:52 | +10 stop | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 11-01 15:51 | +10 stop | HYPE | UP | 0.45 | 0.56 | 0.74 |
| 11-01 15:50 | +10 stop | HYPE | DOWN | 0.56 | 0.39 | -2.05 |
| 11-01 15:50 | +20 | ZEC | DOWN | 0.60 | 0.90 | 2.76 |
| 11-01 15:50 | +10 stop | BTC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-01 15:50 | +10 stop | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-01 15:50 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-01 15:49 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-01 15:49 | +10 | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-01 15:49 | +5 | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-01 15:48 | +15 | BNB | UP | 0.62 | 0.78 | 1.30 |
| 11-01 15:48 | +10 stop | BNB | UP | 0.67 | 0.78 | 0.81 |
| 11-01 15:48 | +10 | BNB | UP | 0.67 | 0.78 | 0.81 |
| 11-01 15:48 | +5 | BNB | UP | 0.67 | 0.73 | 0.30 |
| 11-01 15:48 | +10 stop | BTC | UP | 0.55 | 0.38 | -2.05 |
| 11-01 15:48 | +20 | BTC | UP | 0.55 | open |  |
| 11-01 15:48 | +15 | BTC | UP | 0.55 | open |  |
| 11-01 15:48 | +10 | BTC | UP | 0.55 | open |  |
| 11-01 15:48 | +5 | BTC | UP | 0.55 | open |  |
| 11-01 15:47 | +5 | SOL | UP | 0.65 | open |  |
| 11-01 15:47 | +10 stop | NEAR | UP | 0.30 | 0.54 | 2.07 |
| 11-01 15:47 | +20 | NEAR | UP | 0.31 | 0.54 | 1.97 |
| 11-01 15:47 | +15 | NEAR | UP | 0.31 | 0.54 | 1.97 |
| 11-01 15:47 | +10 | NEAR | UP | 0.31 | 0.54 | 1.97 |
| 11-01 15:47 | +5 | NEAR | UP | 0.32 | 0.54 | 1.86 |
| 11-01 15:47 | +10 stop | BNB | UP | 0.52 | 0.65 | 1.01 |
| 11-01 15:47 | +20 | BNB | UP | 0.52 | 0.73 | 1.83 |
| 11-01 15:47 | +15 | BNB | UP | 0.51 | 0.66 | 1.16 |
| 11-01 15:47 | +10 | BNB | UP | 0.51 | 0.61 | 0.65 |
| 11-01 15:47 | +5 | BNB | UP | 0.51 | 0.61 | 0.65 |
| 11-01 15:47 | +10 stop | DOGE | UP | 0.53 | 0.38 | -1.85 |
| 11-01 15:47 | +20 | DOGE | UP | 0.53 | open |  |
| 11-01 15:47 | +15 | DOGE | UP | 0.53 | open |  |
| 11-01 15:47 | +10 | DOGE | UP | 0.53 | open |  |
| 11-01 15:47 | +5 | DOGE | UP | 0.53 | open |  |
| 11-01 15:47 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-01 15:47 | +15 | ZEC | UP | 0.63 | open |  |
| 11-01 15:47 | +10 | ZEC | UP | 0.63 | open |  |
| 11-01 15:47 | +5 | ZEC | UP | 0.63 | open |  |
| 11-01 15:47 | +10 stop | ETH | UP | 0.53 | 0.30 | -2.63 |
