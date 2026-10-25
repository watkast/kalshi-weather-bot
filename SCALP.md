# Range-Scalp Bot

*Updated Sun Oct 25 13:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33234 | 29001 | 4233 (42) | 5 | $-9300.94 | -4.4% |
| **+10¢** | 24875 | 19976 | 4899 (60) | 6 | $-8257.60 | -5.3% |
| **+15¢** | 20809 | 15534 | 5275 (83) | 8 | $-7439.22 | -5.7% |
| **+20¢** | 18438 | 12914 | 5524 (105) | 8 | $-6555.11 | -5.7% |
| **+10¢ (15¢ stop)** | 40769 | 40709 | 60 (32) | 0 | $-15579.36 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 13:57 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.28 |
| 10-25 13:57 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-25 13:57 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-25 13:57 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-25 13:57 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-25 13:56 | +10 stop | ETH | DOWN | 0.66 | 0.89 | 2.07 |
| 10-25 13:56 | +10 stop | DOGE | UP | 0.61 | 0.37 | -2.74 |
| 10-25 13:56 | +20 | DOGE | UP | 0.61 | open |  |
| 10-25 13:56 | +15 | DOGE | UP | 0.61 | open |  |
| 10-25 13:56 | +10 | DOGE | UP | 0.61 | open |  |
| 10-25 13:56 | +5 | DOGE | UP | 0.61 | open |  |
| 10-25 13:55 | +10 stop | ZEC | UP | 0.66 | 0.48 | -2.14 |
| 10-25 13:55 | +15 | ZEC | UP | 0.66 | open |  |
| 10-25 13:55 | +10 | ZEC | UP | 0.66 | open |  |
| 10-25 13:55 | +5 | ZEC | UP | 0.67 | open |  |
| 10-25 13:55 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-25 13:55 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-25 13:55 | +10 stop | NEAR | DOWN | 0.68 | 0.81 | 1.03 |
| 10-25 13:55 | +10 | NEAR | DOWN | 0.68 | 0.81 | 1.03 |
| 10-25 13:55 | +5 | NEAR | DOWN | 0.68 | 0.81 | 1.03 |
| 10-25 13:55 | +10 | ETH | UP | 0.54 | open |  |
| 10-25 13:55 | +10 stop | NEAR | UP | 0.50 | 0.65 | 1.16 |
| 10-25 13:55 | +10 | NEAR | UP | 0.48 | 0.65 | 1.36 |
| 10-25 13:55 | +5 | NEAR | UP | 0.48 | 0.65 | 1.36 |
| 10-25 13:53 | +10 stop | ETH | UP | 0.66 | 0.48 | -2.14 |
| 10-25 13:53 | +10 stop | SOL | UP | 0.65 | 0.48 | -2.04 |
| 10-25 13:53 | +10 stop | NEAR | UP | 0.61 | 0.73 | 0.92 |
| 10-25 13:53 | +10 | NEAR | UP | 0.61 | 0.73 | 0.91 |
| 10-25 13:53 | +5 | NEAR | UP | 0.59 | 0.68 | 0.59 |
| 10-25 13:52 | +10 stop | SOL | UP | 0.65 | 0.49 | -1.94 |
| 10-25 13:52 | +10 stop | HYPE | UP | 0.53 | 0.29 | -2.73 |
| 10-25 13:50 | +10 stop | BTC | DOWN | 0.61 | 0.28 | -3.62 |
| 10-25 13:50 | +10 stop | NEAR | DOWN | 0.56 | 0.24 | -3.51 |
| 10-25 13:50 | +10 stop | SOL | DOWN | 0.49 | 0.34 | -1.84 |
| 10-25 13:50 | +10 stop | XRP | UP | 0.68 | 0.80 | 0.95 |
| 10-25 13:50 | +10 | XRP | UP | 0.68 | 0.80 | 0.95 |
| 10-25 13:50 | +5 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-25 13:49 | +10 stop | HYPE | DOWN | 0.59 | 0.38 | -2.44 |
| 10-25 13:49 | +10 stop | ETH | DOWN | 0.64 | 0.42 | -2.55 |
| 10-25 13:49 | +5 | ETH | DOWN | 0.64 | 0.89 | 2.28 |
