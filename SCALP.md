# Range-Scalp Bot

*Updated Sun Oct 25 01:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32350 | 28207 | 4143 (41) | 4 | $-9221.16 | -4.5% |
| **+10¢** | 24216 | 19417 | 4799 (59) | 6 | $-8269.97 | -5.4% |
| **+15¢** | 20278 | 15117 | 5161 (82) | 6 | $-7399.94 | -5.8% |
| **+20¢** | 17964 | 12564 | 5400 (104) | 6 | $-6541.74 | -5.8% |
| **+10¢ (15¢ stop)** | 39748 | 39688 | 60 (32) | 5 | $-15189.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 01:33 | +5 | BNB | DOWN | 0.58 | 0.63 | 0.15 |
| 10-25 01:32 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-25 01:32 | +10 stop | BNB | DOWN | 0.59 | open |  |
| 10-25 01:32 | +20 | BNB | DOWN | 0.59 | open |  |
| 10-25 01:32 | +15 | BNB | DOWN | 0.59 | open |  |
| 10-25 01:32 | +10 | BNB | DOWN | 0.59 | open |  |
| 10-25 01:32 | +5 | BNB | DOWN | 0.59 | 0.64 | 0.16 |
| 10-25 01:32 | +10 stop | HYPE | UP | 0.68 | 0.46 | -2.54 |
| 10-25 01:32 | +20 | HYPE | UP | 0.68 | open |  |
| 10-25 01:32 | +15 | HYPE | UP | 0.68 | open |  |
| 10-25 01:32 | +10 | HYPE | UP | 0.68 | open |  |
| 10-25 01:32 | +5 | HYPE | UP | 0.68 | open |  |
| 10-25 01:32 | +10 stop | ETH | DOWN | 0.59 | open |  |
| 10-25 01:32 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-25 01:32 | +10 | ETH | DOWN | 0.59 | open |  |
| 10-25 01:32 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.27 |
| 10-25 01:31 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 10-25 01:31 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-25 01:31 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-25 01:31 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-25 01:31 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-25 01:31 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-25 01:31 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-25 01:31 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-25 01:31 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-25 01:31 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-25 01:31 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 10-25 01:31 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-25 01:31 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-25 01:31 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-25 01:31 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-25 01:30 | +10 stop | ETH | DOWN | 0.56 | 0.70 | 1.07 |
| 10-25 01:30 | +20 | ETH | DOWN | 0.56 | open |  |
| 10-25 01:30 | +15 | ETH | DOWN | 0.56 | 0.73 | 1.38 |
| 10-25 01:30 | +10 | ETH | DOWN | 0.56 | 0.70 | 1.07 |
| 10-25 01:30 | +5 | ETH | DOWN | 0.56 | 0.70 | 1.07 |
| 10-25 01:29 | +10 stop | BTC | DOWN | 0.19 | 0.54 | 3.21 |
| 10-25 01:29 | +10 | BTC | DOWN | 0.18 | 0.54 | 3.27 |
| 10-25 01:29 | +5 | BTC | DOWN | 0.19 | 0.54 | 3.21 |
| 10-25 01:27 | +10 stop | BTC | UP | 0.69 | 0.31 | -4.10 |
