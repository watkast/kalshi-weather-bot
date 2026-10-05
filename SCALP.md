# Range-Scalp Bot

*Updated Mon Oct 05 06:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3449 | 2958 | 491 (3) | 1 | $-1268.89 | -5.8% |
| **+10¢** | 2666 | 2106 | 560 (4) | 2 | $-1141.39 | -6.8% |
| **+15¢** | 2241 | 1646 | 595 (6) | 3 | $-1052.01 | -7.5% |
| **+20¢** | 1998 | 1376 | 622 (11) | 3 | $-934.06 | -7.4% |
| **+10¢ (15¢ stop)** | 4280 | 4279 | 1 (1) | 0 | $-1676.70 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 06:47 | +10 stop | HYPE | UP | 0.70 | 0.84 | 1.11 |
| 10-05 06:46 | +10 stop | BTC | UP | 0.54 | 0.77 | 1.99 |
| 10-05 06:46 | +20 | BTC | UP | 0.54 | 0.77 | 1.99 |
| 10-05 06:46 | +15 | BTC | UP | 0.54 | 0.77 | 1.99 |
| 10-05 06:46 | +10 | BTC | UP | 0.54 | 0.77 | 1.99 |
| 10-05 06:46 | +5 | BTC | UP | 0.54 | 0.59 | 0.15 |
| 10-05 06:46 | +10 stop | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-05 06:46 | +20 | SOL | UP | 0.62 | 0.85 | 2.04 |
| 10-05 06:46 | +15 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-05 06:46 | +10 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-05 06:46 | +5 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-05 06:46 | +10 stop | ZEC | UP | 0.57 | 0.78 | 1.75 |
| 10-05 06:46 | +10 | ZEC | UP | 0.57 | 0.78 | 1.76 |
| 10-05 06:46 | +5 | ZEC | UP | 0.57 | 0.78 | 1.76 |
| 10-05 06:46 | +10 stop | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-05 06:46 | +20 | BNB | UP | 0.59 | 0.79 | 1.71 |
| 10-05 06:46 | +15 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-05 06:46 | +10 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-05 06:46 | +5 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-05 06:46 | +10 stop | DOGE | DOWN | 0.47 | 0.30 | -1.99 |
| 10-05 06:46 | +20 | DOGE | DOWN | 0.47 | open |  |
| 10-05 06:46 | +15 | DOGE | DOWN | 0.47 | open |  |
| 10-05 06:46 | +10 | DOGE | DOWN | 0.47 | open |  |
| 10-05 06:46 | +5 | DOGE | DOWN | 0.47 | 0.54 | 0.38 |
| 10-05 06:46 | +10 stop | NEAR | DOWN | 0.49 | 0.32 | -2.04 |
| 10-05 06:46 | +20 | NEAR | DOWN | 0.49 | open |  |
| 10-05 06:46 | +15 | NEAR | DOWN | 0.49 | open |  |
| 10-05 06:46 | +10 | NEAR | DOWN | 0.49 | open |  |
| 10-05 06:46 | +5 | NEAR | DOWN | 0.49 | open |  |
| 10-05 06:46 | +10 stop | ZEC | DOWN | 0.47 | 0.58 | 0.74 |
| 10-05 06:46 | +20 | ZEC | DOWN | 0.47 | open |  |
| 10-05 06:46 | +15 | ZEC | DOWN | 0.47 | open |  |
| 10-05 06:46 | +10 | ZEC | DOWN | 0.47 | 0.58 | 0.74 |
| 10-05 06:46 | +5 | ZEC | DOWN | 0.47 | 0.58 | 0.74 |
| 10-05 06:42 | +10 stop | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-05 06:42 | +10 stop | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 10-05 06:41 | +10 stop | NEAR | UP | 0.60 | 0.34 | -2.93 |
| 10-05 06:41 | +10 stop | SOL | DOWN | 0.66 | 0.30 | -3.91 |
| 10-05 06:41 | +10 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 10-05 06:41 | +5 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
