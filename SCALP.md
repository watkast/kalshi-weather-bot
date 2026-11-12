# Range-Scalp Bot

*Updated Thu Nov 12 03:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56563 | 49311 | 7252 (98) | 6 | $-15559.92 | -4.4% |
| **+10¢** | 42263 | 33804 | 8459 (128) | 8 | $-14502.39 | -5.5% |
| **+15¢** | 35441 | 26331 | 9110 (162) | 8 | $-13160.59 | -5.9% |
| **+20¢** | 31575 | 22014 | 9561 (212) | 8 | $-11555.19 | -5.8% |
| **+10¢ (15¢ stop)** | 68970 | 68847 | 123 (73) | 0 | $-25477.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 03:39 | +10 stop | NEAR | UP | 0.52 | 0.36 | -1.95 |
| 11-12 03:39 | +5 | NEAR | UP | 0.52 | open |  |
| 11-12 03:38 | +10 stop | NEAR | UP | 0.59 | 0.70 | 0.78 |
| 11-12 03:37 | +10 stop | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
| 11-12 03:36 | +10 stop | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 11-12 03:36 | +10 stop | NEAR | DOWN | 0.56 | 0.37 | -2.25 |
| 11-12 03:36 | +10 stop | ETH | DOWN | 0.55 | 0.69 | 1.07 |
| 11-12 03:35 | +10 stop | ZEC | DOWN | 0.69 | 0.54 | -1.83 |
| 11-12 03:35 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.74 |
| 11-12 03:35 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-12 03:35 | +10 stop | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-12 03:35 | +5 | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-12 03:35 | +10 stop | SOL | UP | 0.57 | 0.39 | -2.15 |
| 11-12 03:35 | +10 stop | ETH | UP | 0.55 | 0.31 | -2.73 |
| 11-12 03:34 | +5 | HYPE | DOWN | 0.54 | 0.67 | 0.96 |
| 11-12 03:34 | +10 stop | NEAR | DOWN | 0.48 | 0.66 | 1.46 |
| 11-12 03:34 | +10 stop | ETH | DOWN | 0.44 | 0.55 | 0.74 |
| 11-12 03:34 | +10 stop | ETH | UP | 0.45 | 0.57 | 0.84 |
| 11-12 03:33 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-12 03:33 | +10 stop | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 11-12 03:33 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-12 03:33 | +10 stop | BNB | DOWN | 0.61 | 0.43 | -2.15 |
| 11-12 03:33 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-12 03:33 | +10 stop | SOL | UP | 0.61 | 0.46 | -1.85 |
| 11-12 03:33 | +20 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +15 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +10 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +5 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +10 stop | NEAR | UP | 0.61 | 0.44 | -2.05 |
| 11-12 03:33 | +5 | NEAR | UP | 0.61 | 0.70 | 0.58 |
| 11-12 03:33 | +10 stop | DOGE | UP | 0.50 | 0.34 | -1.94 |
| 11-12 03:33 | +15 | DOGE | UP | 0.50 | open |  |
| 11-12 03:33 | +10 | DOGE | UP | 0.50 | open |  |
| 11-12 03:33 | +5 | DOGE | UP | 0.50 | 0.57 | 0.34 |
| 11-12 03:32 | +5 | HYPE | UP | 0.53 | 0.61 | 0.45 |
| 11-12 03:32 | +10 stop | XRP | UP | 0.67 | 0.50 | -2.04 |
| 11-12 03:32 | +20 | XRP | UP | 0.67 | open |  |
| 11-12 03:32 | +15 | XRP | UP | 0.67 | open |  |
| 11-12 03:32 | +10 | XRP | UP | 0.67 | open |  |
| 11-12 03:32 | +5 | XRP | UP | 0.67 | open |  |
