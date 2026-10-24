# Range-Scalp Bot

*Updated Sat Oct 24 01:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31240 | 27225 | 4015 (40) | 5 | $-9016.88 | -4.6% |
| **+10¢** | 23376 | 18739 | 4637 (58) | 7 | $-8003.21 | -5.4% |
| **+15¢** | 19558 | 14572 | 4986 (81) | 7 | $-7172.79 | -5.8% |
| **+20¢** | 17327 | 12105 | 5222 (103) | 7 | $-6401.43 | -5.9% |
| **+10¢ (15¢ stop)** | 38342 | 38283 | 59 (32) | 0 | $-14609.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 01:44 | +5 | DOGE | DOWN | 0.09 | 0.57 | 4.56 |
| 10-24 01:44 | +10 stop | DOGE | DOWN | 0.12 | 0.57 | 4.24 |
| 10-24 01:43 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-24 01:43 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 01:43 | +5 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 01:42 | +10 stop | SOL | DOWN | 0.47 | 0.61 | 1.05 |
| 10-24 01:42 | +20 | SOL | DOWN | 0.47 | 0.81 | 3.11 |
| 10-24 01:42 | +15 | SOL | DOWN | 0.47 | 0.81 | 3.11 |
| 10-24 01:42 | +10 | SOL | DOWN | 0.47 | 0.61 | 1.05 |
| 10-24 01:42 | +5 | SOL | DOWN | 0.47 | 0.61 | 1.05 |
| 10-24 01:41 | +10 stop | BTC | UP | 0.65 | 0.82 | 1.43 |
| 10-24 01:41 | +10 stop | NEAR | UP | 0.50 | 0.63 | 0.95 |
| 10-24 01:41 | +5 | NEAR | UP | 0.49 | 0.56 | 0.34 |
| 10-24 01:41 | +10 stop | DOGE | DOWN | 0.51 | 0.26 | -2.82 |
| 10-24 01:41 | +20 | DOGE | DOWN | 0.51 | open |  |
| 10-24 01:41 | +15 | DOGE | DOWN | 0.51 | open |  |
| 10-24 01:41 | +10 | DOGE | DOWN | 0.51 | open |  |
| 10-24 01:41 | +5 | DOGE | DOWN | 0.51 | 0.56 | 0.14 |
| 10-24 01:41 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 10-24 01:40 | +10 stop | ETH | UP | 0.70 | 0.55 | -1.83 |
| 10-24 01:40 | +5 | NEAR | DOWN | 0.50 | 0.58 | 0.44 |
| 10-24 01:40 | +10 stop | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 10-24 01:40 | +15 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 10-24 01:40 | +10 | ZEC | DOWN | 0.61 | 0.79 | 1.51 |
| 10-24 01:40 | +5 | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 10-24 01:39 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-24 01:39 | +10 stop | ETH | DOWN | 0.61 | 0.44 | -2.05 |
| 10-24 01:39 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-24 01:39 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-24 01:39 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-24 01:39 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-24 01:39 | +10 stop | BTC | DOWN | 0.69 | 0.51 | -2.13 |
| 10-24 01:39 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-24 01:39 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-24 01:39 | +10 | BTC | DOWN | 0.69 | open |  |
| 10-24 01:39 | +5 | BTC | DOWN | 0.69 | open |  |
| 10-24 01:39 | +10 stop | NEAR | DOWN | 0.55 | 0.35 | -2.34 |
| 10-24 01:39 | +20 | NEAR | DOWN | 0.55 | open |  |
| 10-24 01:39 | +15 | NEAR | DOWN | 0.55 | open |  |
| 10-24 01:39 | +10 | NEAR | DOWN | 0.55 | open |  |
