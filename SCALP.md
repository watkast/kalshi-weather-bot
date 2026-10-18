# Range-Scalp Bot

*Updated Sun Oct 18 14:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22663 | 19730 | 2933 (29) | 0 | $-6600.61 | -4.6% |
| **+10¢** | 17051 | 13666 | 3385 (43) | 1 | $-5849.73 | -5.5% |
| **+15¢** | 14277 | 10624 | 3653 (64) | 1 | $-5338.40 | -6.0% |
| **+20¢** | 12639 | 8815 | 3824 (82) | 1 | $-4738.62 | -6.0% |
| **+10¢ (15¢ stop)** | 27859 | 27809 | 50 (29) | 0 | $-10636.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 14:01 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.81 |
| 10-18 14:01 | +20 | DOGE | DOWN | 0.69 | 0.91 | 1.95 |
| 10-18 14:01 | +15 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 10-18 14:01 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-18 14:01 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-18 14:01 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-18 14:01 | +20 | SOL | DOWN | 0.70 | 0.93 | 2.05 |
| 10-18 14:01 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 10-18 14:01 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-18 14:01 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 10-18 14:01 | +10 stop | NEAR | DOWN | 0.71 | 0.51 | -2.33 |
| 10-18 14:01 | +20 | NEAR | DOWN | 0.71 | 0.91 | 1.83 |
| 10-18 14:01 | +15 | NEAR | DOWN | 0.71 | 0.91 | 1.78 |
| 10-18 14:01 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-18 14:01 | +5 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-18 14:01 | +10 stop | ETH | UP | 0.47 | 0.26 | -2.42 |
| 10-18 14:01 | +20 | ETH | UP | 0.47 | open |  |
| 10-18 14:01 | +15 | ETH | UP | 0.47 | open |  |
| 10-18 14:01 | +10 | ETH | UP | 0.47 | open |  |
| 10-18 14:01 | +5 | ETH | UP | 0.47 | 0.54 | 0.34 |
| 10-18 13:55 | +10 stop | BNB | UP | 0.70 | 0.84 | 1.18 |
| 10-18 13:55 | +10 | BNB | UP | 0.70 | 0.84 | 1.18 |
| 10-18 13:55 | +5 | BNB | UP | 0.69 | 0.84 | 1.27 |
| 10-18 13:52 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.94 |
| 10-18 13:52 | +5 | NEAR | DOWN | 0.64 | 0.76 | 0.94 |
| 10-18 13:52 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-18 13:52 | +15 | BNB | UP | 0.66 | 0.84 | 1.54 |
| 10-18 13:52 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-18 13:52 | +5 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-18 13:51 | +5 | NEAR | UP | 0.47 | 0.53 | 0.24 |
| 10-18 13:49 | +5 | BNB | UP | 0.71 | 0.80 | 0.63 |
| 10-18 13:48 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-18 13:48 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-18 13:48 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 10-18 13:47 | +5 | XRP | UP | 0.69 | 0.77 | 0.52 |
| 10-18 13:47 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-18 13:47 | +10 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-18 13:47 | +5 | BTC | UP | 0.70 | 0.78 | 0.52 |
| 10-18 13:46 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 10-18 13:46 | +20 | BTC | UP | 0.62 | 0.83 | 1.83 |
