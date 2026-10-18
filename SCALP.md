# Range-Scalp Bot

*Updated Sun Oct 18 15:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22690 | 19751 | 2939 (29) | 0 | $-6628.52 | -4.6% |
| **+10¢** | 17073 | 13680 | 3393 (43) | 1 | $-5883.69 | -5.5% |
| **+15¢** | 14297 | 10636 | 3661 (64) | 2 | $-5365.02 | -6.0% |
| **+20¢** | 12658 | 8826 | 3832 (82) | 3 | $-4763.56 | -6.0% |
| **+10¢ (15¢ stop)** | 27901 | 27851 | 50 (29) | 1 | $-10654.68 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 15:01 | +10 stop | HYPE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-18 15:01 | +20 | HYPE | DOWN | 0.46 | open |  |
| 10-18 15:01 | +15 | HYPE | DOWN | 0.46 | 0.62 | 1.25 |
| 10-18 15:01 | +10 | HYPE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-18 15:01 | +5 | HYPE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-18 15:01 | +10 stop | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-18 15:01 | +20 | DOGE | UP | 0.71 | open |  |
| 10-18 15:01 | +15 | DOGE | UP | 0.71 | open |  |
| 10-18 15:01 | +10 | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-18 15:01 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 10-18 15:01 | +10 stop | NEAR | UP | 0.66 | open |  |
| 10-18 15:01 | +20 | NEAR | UP | 0.66 | open |  |
| 10-18 15:01 | +15 | NEAR | UP | 0.66 | open |  |
| 10-18 15:01 | +10 | NEAR | UP | 0.66 | open |  |
| 10-18 15:01 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-18 14:59 | +10 stop | BTC | UP | 0.67 | 0.22 | -4.79 |
| 10-18 14:57 | +10 stop | SOL | UP | 0.63 | 0.79 | 1.31 |
| 10-18 14:56 | +10 stop | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-18 14:53 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-18 14:53 | +5 | NEAR | DOWN | 0.61 | yes | -6.27 |
| 10-18 14:53 | +10 stop | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-18 14:52 | +10 stop | HYPE | UP | 0.63 | 0.38 | -2.84 |
| 10-18 14:51 | +5 | HYPE | UP | 0.66 | 0.83 | 1.44 |
| 10-18 14:51 | +10 stop | BNB | DOWN | 0.54 | 0.66 | 0.86 |
| 10-18 14:51 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 10-18 14:51 | +10 stop | BTC | UP | 0.62 | 0.44 | -2.15 |
| 10-18 14:50 | +10 stop | HYPE | UP | 0.56 | 0.68 | 0.86 |
| 10-18 14:50 | +5 | HYPE | UP | 0.56 | 0.64 | 0.45 |
| 10-18 14:50 | +10 stop | XRP | UP | 0.65 | 0.78 | 1.01 |
| 10-18 14:49 | +10 stop | BTC | UP | 0.47 | 0.57 | 0.64 |
| 10-18 14:49 | +10 stop | NEAR | DOWN | 0.55 | 0.33 | -2.54 |
| 10-18 14:49 | +20 | NEAR | DOWN | 0.55 | yes | -5.72 |
| 10-18 14:49 | +15 | NEAR | DOWN | 0.55 | yes | -5.72 |
| 10-18 14:49 | +10 | NEAR | DOWN | 0.55 | yes | -5.72 |
| 10-18 14:49 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.21 |
| 10-18 14:49 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
| 10-18 14:48 | +5 | BNB | UP | 0.62 | 0.71 | 0.54 |
| 10-18 14:48 | +10 stop | BNB | UP | 0.57 | 0.42 | -1.86 |
| 10-18 14:48 | +10 | BNB | UP | 0.57 | 0.71 | 1.07 |
| 10-18 14:48 | +5 | BNB | UP | 0.57 | 0.65 | 0.46 |
