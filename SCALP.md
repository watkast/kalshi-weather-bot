# Range-Scalp Bot

*Updated Wed Nov 25 15:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71714 | 62588 | 9126 (158) | 6 | $-19143.71 | -4.2% |
| **+10¢** | 53489 | 42835 | 10654 (203) | 8 | $-17728.61 | -5.3% |
| **+15¢** | 44801 | 33330 | 11471 (260) | 9 | $-15774.46 | -5.6% |
| **+20¢** | 39888 | 27809 | 12079 (326) | 9 | $-14161.02 | -5.7% |
| **+10¢ (15¢ stop)** | 87336 | 87127 | 209 (128) | 1 | $-32110.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 15:51 | +5 | SOL | UP | 0.53 | 0.80 | 2.36 |
| 11-25 15:50 | +5 | SOL | UP | 0.52 | 0.61 | 0.55 |
| 11-25 15:50 | +10 stop | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 11-25 15:50 | +10 stop | BTC | UP | 0.47 | 0.63 | 1.25 |
| 11-25 15:50 | +10 | BTC | UP | 0.47 | 0.63 | 1.25 |
| 11-25 15:50 | +5 | BTC | UP | 0.47 | 0.54 | 0.34 |
| 11-25 15:49 | +10 stop | SOL | UP | 0.53 | 0.80 | 2.40 |
| 11-25 15:49 | +5 | SOL | UP | 0.54 | 0.59 | 0.15 |
| 11-25 15:49 | +10 stop | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 11-25 15:49 | +10 stop | BNB | UP | 0.70 | open |  |
| 11-25 15:49 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
| 11-25 15:49 | +5 | ETH | UP | 0.63 | 0.72 | 0.58 |
| 11-25 15:49 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 11-25 15:47 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-25 15:47 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-25 15:47 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-25 15:47 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-25 15:47 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-25 15:46 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 11-25 15:46 | +20 | SOL | DOWN | 0.68 | open |  |
| 11-25 15:46 | +15 | SOL | DOWN | 0.69 | open |  |
| 11-25 15:46 | +10 | SOL | DOWN | 0.69 | open |  |
| 11-25 15:46 | +5 | SOL | DOWN | 0.68 | 0.76 | 0.51 |
| 11-25 15:46 | +10 stop | ZEC | DOWN | 0.66 | 0.41 | -2.83 |
| 11-25 15:46 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-25 15:46 | +15 | ZEC | DOWN | 0.67 | open |  |
| 11-25 15:46 | +10 | ZEC | DOWN | 0.66 | open |  |
| 11-25 15:46 | +5 | ZEC | DOWN | 0.66 | open |  |
| 11-25 15:46 | +10 stop | NEAR | DOWN | 0.64 | 0.38 | -2.94 |
| 11-25 15:46 | +20 | NEAR | DOWN | 0.63 | open |  |
| 11-25 15:46 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-25 15:46 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-25 15:46 | +5 | NEAR | DOWN | 0.64 | open |  |
| 11-25 15:46 | +10 stop | BNB | DOWN | 0.66 | 0.45 | -2.44 |
| 11-25 15:46 | +20 | BNB | DOWN | 0.66 | open |  |
| 11-25 15:46 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-25 15:46 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-25 15:46 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-25 15:46 | +10 stop | HYPE | DOWN | 0.63 | 0.32 | -3.45 |
| 11-25 15:46 | +20 | HYPE | DOWN | 0.65 | open |  |
