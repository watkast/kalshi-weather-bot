# Range-Scalp Bot

*Updated Sun Oct 25 13:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33175 | 28954 | 4221 (42) | 4 | $-9248.52 | -4.4% |
| **+10¢** | 24833 | 19946 | 4887 (60) | 5 | $-8208.62 | -5.3% |
| **+15¢** | 20778 | 15515 | 5263 (83) | 5 | $-7395.25 | -5.7% |
| **+20¢** | 18408 | 12897 | 5511 (105) | 8 | $-6510.18 | -5.6% |
| **+10¢ (15¢ stop)** | 40693 | 40633 | 60 (32) | 3 | $-15515.56 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 13:07 | +5 | DOGE | UP | 0.71 | open |  |
| 10-25 13:07 | +10 stop | DOGE | UP | 0.71 | open |  |
| 10-25 13:07 | +10 stop | ZEC | DOWN | 0.53 | open |  |
| 10-25 13:07 | +5 | ZEC | DOWN | 0.54 | 0.59 | 0.19 |
| 10-25 13:07 | +10 stop | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-25 13:07 | +20 | SOL | DOWN | 0.54 | open |  |
| 10-25 13:07 | +15 | SOL | DOWN | 0.54 | open |  |
| 10-25 13:07 | +10 | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-25 13:07 | +5 | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-25 13:07 | +10 stop | BTC | DOWN | 0.50 | open |  |
| 10-25 13:07 | +10 | BTC | DOWN | 0.50 | open |  |
| 10-25 13:06 | +10 stop | HYPE | DOWN | 0.67 | 0.29 | -4.11 |
| 10-25 13:06 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-25 13:06 | +10 stop | NEAR | DOWN | 0.59 | 0.39 | -2.34 |
| 10-25 13:05 | +10 stop | XRP | DOWN | 0.50 | 0.31 | -2.23 |
| 10-25 13:05 | +20 | XRP | DOWN | 0.50 | open |  |
| 10-25 13:05 | +15 | XRP | DOWN | 0.48 | open |  |
| 10-25 13:05 | +5 | XRP | DOWN | 0.48 | 0.56 | 0.44 |
| 10-25 13:05 | +5 | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 10-25 13:04 | +10 stop | ETH | DOWN | 0.67 | 0.47 | -2.34 |
| 10-25 13:04 | +10 stop | DOGE | DOWN | 0.66 | 0.45 | -2.44 |
| 10-25 13:04 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-25 13:04 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-25 13:04 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-25 13:04 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-25 13:04 | +5 | XRP | DOWN | 0.71 | 0.80 | 0.63 |
| 10-25 13:03 | +10 stop | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 10-25 13:03 | +10 stop | HYPE | DOWN | 0.58 | 0.72 | 1.03 |
| 10-25 13:03 | +5 | HYPE | DOWN | 0.58 | 0.72 | 1.03 |
| 10-25 13:03 | +10 stop | ETH | UP | 0.64 | 0.49 | -1.85 |
| 10-25 13:03 | +10 | ETH | UP | 0.64 | 0.81 | 1.42 |
| 10-25 13:03 | +5 | ETH | UP | 0.64 | 0.72 | 0.48 |
| 10-25 13:03 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 13:03 | +5 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 13:03 | +10 stop | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-25 13:03 | +10 | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-25 13:03 | +10 stop | DOGE | DOWN | 0.54 | 0.64 | 0.65 |
| 10-25 13:03 | +10 | DOGE | DOWN | 0.54 | 0.64 | 0.65 |
| 10-25 13:03 | +5 | DOGE | DOWN | 0.54 | 0.64 | 0.65 |
| 10-25 13:03 | +10 stop | ETH | DOWN | 0.43 | 0.63 | 1.65 |
