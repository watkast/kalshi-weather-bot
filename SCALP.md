# Range-Scalp Bot

*Updated Sun Oct 04 20:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2742 | 2358 | 384 (3) | 3 | $-946.70 | -5.4% |
| **+10¢** | 2139 | 1707 | 432 (4) | 3 | $-786.27 | -5.8% |
| **+15¢** | 1796 | 1342 | 454 (5) | 5 | $-652.98 | -5.8% |
| **+20¢** | 1598 | 1122 | 476 (9) | 5 | $-567.23 | -5.6% |
| **+10¢ (15¢ stop)** | 3405 | 3404 | 1 (1) | 3 | $-1294.83 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 20:02 | +10 stop | BTC | UP | 0.58 | open |  |
| 10-04 20:02 | +10 stop | BNB | UP | 0.50 | open |  |
| 10-04 20:02 | +10 stop | ZEC | DOWN | 0.59 | open |  |
| 10-04 20:02 | +15 | ZEC | DOWN | 0.59 | open |  |
| 10-04 20:02 | +10 | ZEC | DOWN | 0.59 | open |  |
| 10-04 20:02 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-04 20:01 | +10 stop | BTC | DOWN | 0.66 | 0.37 | -3.23 |
| 10-04 20:01 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-04 20:01 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-04 20:01 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-04 20:01 | +5 | BTC | DOWN | 0.66 | open |  |
| 10-04 20:01 | +10 stop | BNB | DOWN | 0.68 | 0.42 | -2.94 |
| 10-04 20:01 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-04 20:01 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-04 20:01 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-04 20:01 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-04 20:00 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-04 20:00 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-04 20:00 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-04 20:00 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-04 20:00 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 10-04 20:00 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-04 20:00 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-04 20:00 | +15 | HYPE | DOWN | 0.62 | open |  |
| 10-04 20:00 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-04 20:00 | +5 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-04 20:00 | +10 stop | NEAR | DOWN | 0.60 | 0.79 | 1.61 |
| 10-04 20:00 | +20 | NEAR | DOWN | 0.60 | 0.85 | 2.24 |
| 10-04 20:00 | +15 | NEAR | DOWN | 0.60 | 0.79 | 1.61 |
| 10-04 20:00 | +10 | NEAR | DOWN | 0.60 | 0.79 | 1.61 |
| 10-04 20:00 | +5 | NEAR | DOWN | 0.60 | 0.79 | 1.61 |
| 10-04 20:00 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.93 |
| 10-04 20:00 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-04 20:00 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.24 |
| 10-04 20:00 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.93 |
| 10-04 20:00 | +5 | ZEC | DOWN | 0.64 | 0.76 | 0.87 |
| 10-04 19:57 | +10 stop | HYPE | UP | 0.58 | 0.23 | -3.81 |
| 10-04 19:56 | +10 stop | BTC | DOWN | 0.54 | 0.71 | 1.37 |
| 10-04 19:56 | +10 stop | HYPE | DOWN | 0.69 | 0.45 | -2.73 |
| 10-04 19:55 | +10 stop | ETH | DOWN | 0.56 | 0.74 | 1.48 |
