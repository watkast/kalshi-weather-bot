# Range-Scalp Bot

*Updated Sat Nov 21 01:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66808 | 58307 | 8501 (128) | 4 | $-17948.93 | -4.3% |
| **+10¢** | 49894 | 39959 | 9935 (170) | 5 | $-16673.15 | -5.3% |
| **+15¢** | 41845 | 31133 | 10712 (217) | 2 | $-14965.18 | -5.7% |
| **+20¢** | 37244 | 25992 | 11252 (273) | 3 | $-13278.08 | -5.7% |
| **+10¢ (15¢ stop)** | 81362 | 81196 | 166 (100) | 0 | $-30011.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 01:12 | +10 stop | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 11-21 01:12 | +10 | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 11-21 01:12 | +5 | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 11-21 01:12 | +10 stop | NEAR | DOWN | 0.44 | 0.55 | 0.74 |
| 11-21 01:12 | +15 | NEAR | DOWN | 0.44 | 0.93 | 4.67 |
| 11-21 01:12 | +10 | NEAR | DOWN | 0.44 | 0.55 | 0.74 |
| 11-21 01:12 | +5 | NEAR | DOWN | 0.44 | 0.55 | 0.74 |
| 11-21 01:11 | +10 stop | ETH | UP | 0.58 | 0.80 | 1.90 |
| 11-21 01:11 | +5 | ETH | UP | 0.58 | 0.80 | 1.90 |
| 11-21 01:11 | +10 stop | HYPE | UP | 0.68 | 0.91 | 2.05 |
| 11-21 01:11 | +10 stop | DOGE | UP | 0.56 | 0.73 | 1.40 |
| 11-21 01:10 | +5 | ETH | DOWN | 0.43 | 0.57 | 1.04 |
| 11-21 01:10 | +10 stop | ETH | DOWN | 0.46 | 0.57 | 0.74 |
| 11-21 01:10 | +10 stop | BNB | DOWN | 0.68 | 0.43 | -2.84 |
| 11-21 01:10 | +10 stop | BTC | UP | 0.67 | 0.80 | 1.02 |
| 11-21 01:10 | +20 | BTC | UP | 0.67 | 0.88 | 1.86 |
| 11-21 01:10 | +15 | BTC | UP | 0.67 | 0.86 | 1.65 |
| 11-21 01:09 | +10 stop | DOGE | UP | 0.39 | 0.56 | 1.35 |
| 11-21 01:09 | +10 stop | ETH | UP | 0.51 | 0.65 | 1.06 |
| 11-21 01:09 | +5 | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 11-21 01:08 | +10 stop | ETH | DOWN | 0.59 | 0.36 | -2.64 |
| 11-21 01:08 | +10 | ETH | DOWN | 0.59 | open |  |
| 11-21 01:08 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 11-21 01:08 | +10 stop | BTC | UP | 0.60 | 0.74 | 1.09 |
| 11-21 01:08 | +10 stop | ZEC | DOWN | 0.48 | 0.32 | -1.94 |
| 11-21 01:07 | +10 stop | DOGE | DOWN | 0.62 | 0.32 | -3.33 |
| 11-21 01:07 | +10 stop | SOL | DOWN | 0.65 | 0.37 | -3.13 |
| 11-21 01:07 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-21 01:07 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.31 |
| 11-21 01:06 | +10 stop | ETH | DOWN | 0.58 | 0.72 | 1.07 |
| 11-21 01:06 | +10 | ETH | DOWN | 0.58 | 0.72 | 1.07 |
| 11-21 01:06 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 11-21 01:06 | +10 stop | ZEC | DOWN | 0.69 | 0.44 | -2.83 |
| 11-21 01:06 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-21 01:06 | +10 stop | HYPE | DOWN | 0.48 | 0.33 | -1.87 |
| 11-21 01:06 | +10 stop | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-21 01:06 | +15 | NEAR | DOWN | 0.65 | 0.84 | 1.64 |
| 11-21 01:06 | +10 | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-21 01:06 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 11-21 01:05 | +10 stop | DOGE | DOWN | 0.67 | 0.51 | -1.94 |
