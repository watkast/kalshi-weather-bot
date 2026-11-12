# Range-Scalp Bot

*Updated Thu Nov 12 22:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57410 | 50064 | 7346 (101) | 1 | $-15675.82 | -4.3% |
| **+10¢** | 42907 | 34330 | 8577 (133) | 2 | $-14618.94 | -5.4% |
| **+15¢** | 35973 | 26742 | 9231 (167) | 2 | $-13188.79 | -5.8% |
| **+20¢** | 32051 | 22366 | 9685 (217) | 2 | $-11537.95 | -5.7% |
| **+10¢ (15¢ stop)** | 70003 | 69875 | 128 (78) | 0 | $-25820.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 22:41 | +10 stop | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-12 22:41 | +20 | ETH | DOWN | 0.59 | 0.90 | 2.89 |
| 11-12 22:41 | +15 | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-12 22:41 | +10 | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-12 22:41 | +5 | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-12 22:40 | +5 | BNB | UP | 0.56 | 0.77 | 1.84 |
| 11-12 22:40 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-12 22:40 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-12 22:40 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-12 22:40 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-12 22:39 | +10 stop | BNB | DOWN | 0.47 | 0.19 | -3.09 |
| 11-12 22:39 | +20 | BNB | DOWN | 0.47 | open |  |
| 11-12 22:39 | +15 | BNB | DOWN | 0.48 | open |  |
| 11-12 22:39 | +10 | BNB | DOWN | 0.49 | open |  |
| 11-12 22:39 | +5 | BNB | DOWN | 0.47 | 0.53 | 0.24 |
| 11-12 22:38 | +10 stop | NEAR | UP | 0.65 | 0.78 | 1.01 |
| 11-12 22:36 | +10 stop | NEAR | UP | 0.67 | 0.50 | -2.04 |
| 11-12 22:36 | +10 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-12 22:36 | +5 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-12 22:36 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-12 22:36 | +15 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 11-12 22:36 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-12 22:34 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 22:34 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-12 22:34 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-12 22:34 | +10 stop | XRP | UP | 0.49 | 0.26 | -2.62 |
| 11-12 22:33 | +5 | XRP | UP | 0.56 | open |  |
| 11-12 22:33 | +10 stop | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-12 22:33 | +20 | NEAR | UP | 0.67 | 0.89 | 1.97 |
| 11-12 22:33 | +15 | NEAR | UP | 0.67 | 0.89 | 1.97 |
| 11-12 22:33 | +10 | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-12 22:33 | +5 | NEAR | UP | 0.67 | 0.76 | 0.61 |
| 11-12 22:33 | +10 stop | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 11-12 22:33 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 11-12 22:33 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-12 22:33 | +10 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-12 22:33 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 11-12 22:32 | +5 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-12 22:32 | +10 stop | XRP | DOWN | 0.55 | 0.39 | -1.95 |
| 11-12 22:32 | +20 | XRP | DOWN | 0.55 | 0.76 | 1.79 |
