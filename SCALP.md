# Range-Scalp Bot

*Updated Fri Nov 27 07:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73512 | 64155 | 9357 (165) | 4 | $-19592.26 | -4.2% |
| **+10¢** | 54777 | 43850 | 10927 (210) | 5 | $-18225.29 | -5.3% |
| **+15¢** | 45868 | 34099 | 11769 (268) | 6 | $-16325.97 | -5.7% |
| **+20¢** | 40818 | 28426 | 12392 (334) | 6 | $-14730.44 | -5.8% |
| **+10¢ (15¢ stop)** | 89535 | 89323 | 212 (129) | 1 | $-33133.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 07:14 | +10 stop | SOL | UP | 0.60 | open |  |
| 11-27 07:14 | +10 | SOL | UP | 0.67 | open |  |
| 11-27 07:14 | +5 | SOL | UP | 0.66 | open |  |
| 11-27 07:13 | +10 stop | SOL | DOWN | 0.28 | 0.68 | 3.75 |
| 11-27 07:13 | +10 | SOL | DOWN | 0.27 | 0.68 | 3.80 |
| 11-27 07:13 | +5 | SOL | DOWN | 0.27 | 0.68 | 3.80 |
| 11-27 07:13 | +10 stop | ETH | UP | 0.57 | 0.71 | 1.07 |
| 11-27 07:13 | +20 | ETH | UP | 0.63 | 0.92 | 2.63 |
| 11-27 07:13 | +15 | ETH | UP | 0.65 | 0.92 | 2.46 |
| 11-27 07:13 | +10 | ETH | UP | 0.66 | 0.92 | 2.39 |
| 11-27 07:13 | +5 | ETH | UP | 0.63 | 0.71 | 0.48 |
| 11-27 07:11 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.84 |
| 11-27 07:11 | +10 | SOL | DOWN | 0.60 | 0.72 | 0.91 |
| 11-27 07:11 | +10 stop | NEAR | DOWN | 0.47 | 0.57 | 0.64 |
| 11-27 07:10 | +15 | DOGE | UP | 0.64 | 0.86 | 1.94 |
| 11-27 07:10 | +10 stop | DOGE | UP | 0.52 | 0.71 | 1.55 |
| 11-27 07:10 | +10 | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 11-27 07:10 | +5 | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 11-27 07:09 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-27 07:09 | +15 | DOGE | UP | 0.52 | 0.69 | 1.37 |
| 11-27 07:09 | +10 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-27 07:09 | +5 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-27 07:09 | +10 stop | NEAR | UP | 0.56 | 0.34 | -2.54 |
| 11-27 07:09 | +10 | NEAR | UP | 0.56 | 0.77 | 1.79 |
| 11-27 07:09 | +5 | NEAR | UP | 0.56 | 0.77 | 1.79 |
| 11-27 07:09 | +10 stop | ZEC | DOWN | 0.54 | 0.37 | -2.05 |
| 11-27 07:09 | +10 stop | ETH | DOWN | 0.70 | 0.83 | 1.07 |
| 11-27 07:09 | +10 stop | BTC | UP | 0.66 | 0.49 | -2.04 |
| 11-27 07:08 | +10 stop | SOL | DOWN | 0.55 | 0.71 | 1.27 |
| 11-27 07:07 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 11-27 07:07 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-27 07:07 | +10 stop | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-27 07:07 | +15 | NEAR | UP | 0.63 | 0.81 | 1.52 |
| 11-27 07:07 | +10 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-27 07:07 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 11-27 07:06 | +10 stop | ETH | DOWN | 0.63 | 0.47 | -1.95 |
| 11-27 07:06 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.24 |
| 11-27 07:06 | +10 stop | SOL | DOWN | 0.64 | 0.49 | -1.85 |
| 11-27 07:06 | +10 stop | ZEC | DOWN | 0.68 | 0.44 | -2.74 |
| 11-27 07:06 | +5 | DOGE | UP | 0.63 | 0.73 | 0.69 |
