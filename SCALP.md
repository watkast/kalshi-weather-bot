# Range-Scalp Bot

*Updated Sun Oct 18 18:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22823 | 19869 | 2954 (29) | 0 | $-6650.01 | -4.6% |
| **+10¢** | 17167 | 13756 | 3411 (43) | 0 | $-5910.42 | -5.5% |
| **+15¢** | 14384 | 10702 | 3682 (64) | 0 | $-5392.76 | -6.0% |
| **+20¢** | 12735 | 8883 | 3852 (82) | 0 | $-4769.80 | -6.0% |
| **+10¢ (15¢ stop)** | 28082 | 28032 | 50 (29) | 0 | $-10737.27 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 18:27 | +10 | NEAR | UP | 0.70 | 0.80 | 0.74 |
| 10-18 18:27 | +5 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 10-18 18:27 | +10 stop | SOL | DOWN | 0.42 | 0.59 | 1.35 |
| 10-18 18:27 | +10 stop | XRP | UP | 0.56 | 0.85 | 2.63 |
| 10-18 18:27 | +20 | XRP | UP | 0.56 | 0.85 | 2.63 |
| 10-18 18:27 | +15 | XRP | UP | 0.56 | 0.85 | 2.63 |
| 10-18 18:27 | +10 | XRP | UP | 0.56 | 0.85 | 2.63 |
| 10-18 18:27 | +5 | XRP | UP | 0.56 | 0.65 | 0.56 |
| 10-18 18:25 | +10 stop | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-18 18:25 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-18 18:25 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-18 18:25 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-18 18:25 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-18 18:25 | +10 stop | SOL | UP | 0.58 | 0.41 | -2.05 |
| 10-18 18:25 | +20 | SOL | UP | 0.58 | 0.89 | 2.85 |
| 10-18 18:25 | +15 | SOL | UP | 0.58 | 0.89 | 2.85 |
| 10-18 18:25 | +10 | SOL | UP | 0.58 | 0.89 | 2.85 |
| 10-18 18:25 | +5 | SOL | UP | 0.58 | 0.63 | 0.15 |
| 10-18 16:57 | +10 stop | BNB | DOWN | 0.50 | 0.75 | 2.18 |
| 10-18 16:57 | +10 stop | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-18 16:57 | +20 | XRP | DOWN | 0.67 | 0.91 | 2.17 |
| 10-18 16:57 | +15 | XRP | DOWN | 0.67 | 0.91 | 2.17 |
| 10-18 16:57 | +10 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-18 16:57 | +5 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-18 16:56 | +10 stop | ETH | DOWN | 0.68 | 0.44 | -2.74 |
| 10-18 16:56 | +10 stop | BNB | DOWN | 0.50 | 0.29 | -2.43 |
| 10-18 16:55 | +10 stop | SOL | UP | 0.67 | 0.89 | 1.97 |
| 10-18 16:55 | +10 stop | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-18 16:52 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.05 |
| 10-18 16:51 | +10 stop | XRP | UP | 0.61 | 0.46 | -1.85 |
| 10-18 16:51 | +10 stop | ETH | UP | 0.59 | 0.33 | -2.93 |
| 10-18 16:51 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.70 |
| 10-18 16:51 | +10 stop | BNB | DOWN | 0.56 | 0.41 | -1.85 |
| 10-18 16:50 | +10 stop | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-18 16:50 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-18 16:49 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-18 16:48 | +10 stop | HYPE | UP | 0.64 | 0.39 | -2.80 |
| 10-18 16:48 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 10-18 16:48 | +10 stop | NEAR | DOWN | 0.50 | 0.35 | -1.84 |
| 10-18 16:47 | +10 stop | ZEC | DOWN | 0.62 | 0.47 | -1.85 |
