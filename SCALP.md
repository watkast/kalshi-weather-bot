# Range-Scalp Bot

*Updated Mon Oct 12 23:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14004 | 12119 | 1885 (26) | 4 | $-4457.31 | -5.1% |
| **+10¢** | 10599 | 8406 | 2193 (38) | 5 | $-4199.09 | -6.3% |
| **+15¢** | 8909 | 6562 | 2347 (56) | 5 | $-3734.71 | -6.7% |
| **+20¢** | 7926 | 5482 | 2444 (71) | 5 | $-3188.85 | -6.4% |
| **+10¢ (15¢ stop)** | 17183 | 17134 | 49 (29) | 0 | $-6665.45 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 23:36 | +10 stop | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 10-12 23:33 | +10 stop | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 10-12 23:32 | +10 stop | BNB | DOWN | 0.55 | 0.67 | 0.86 |
| 10-12 23:32 | +10 stop | SOL | DOWN | 0.57 | 0.75 | 1.48 |
| 10-12 23:32 | +10 stop | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 10-12 23:32 | +5 | SOL | DOWN | 0.57 | 0.75 | 1.48 |
| 10-12 23:32 | +10 stop | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 10-12 23:32 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-12 23:32 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 10-12 23:32 | +15 | NEAR | DOWN | 0.65 | 0.83 | 1.54 |
| 10-12 23:32 | +10 | NEAR | DOWN | 0.62 | 0.75 | 0.95 |
| 10-12 23:32 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.23 |
| 10-12 23:32 | +10 stop | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-12 23:32 | +20 | BTC | DOWN | 0.65 | 0.86 | 1.85 |
| 10-12 23:32 | +15 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-12 23:32 | +10 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-12 23:32 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 10-12 23:32 | +10 stop | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-12 23:32 | +20 | DOGE | DOWN | 0.59 | 0.80 | 1.81 |
| 10-12 23:32 | +15 | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-12 23:32 | +10 | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-12 23:32 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 10-12 23:31 | +10 stop | SOL | UP | 0.57 | 0.40 | -2.05 |
| 10-12 23:31 | +20 | SOL | UP | 0.57 | open |  |
| 10-12 23:31 | +15 | SOL | UP | 0.57 | open |  |
| 10-12 23:31 | +10 | SOL | UP | 0.57 | open |  |
| 10-12 23:31 | +5 | SOL | UP | 0.57 | 0.63 | 0.25 |
| 10-12 23:31 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 10-12 23:31 | +20 | ETH | UP | 0.58 | open |  |
| 10-12 23:31 | +15 | ETH | UP | 0.58 | open |  |
| 10-12 23:31 | +10 | ETH | UP | 0.58 | open |  |
| 10-12 23:31 | +5 | ETH | UP | 0.58 | open |  |
| 10-12 23:30 | +10 stop | XRP | UP | 0.66 | 0.50 | -1.94 |
| 10-12 23:30 | +20 | XRP | UP | 0.66 | open |  |
| 10-12 23:30 | +15 | XRP | UP | 0.66 | open |  |
| 10-12 23:30 | +10 | XRP | UP | 0.66 | open |  |
| 10-12 23:30 | +5 | XRP | UP | 0.66 | open |  |
| 10-12 23:30 | +10 stop | BNB | UP | 0.59 | 0.36 | -2.64 |
| 10-12 23:30 | +20 | BNB | UP | 0.59 | open |  |
| 10-12 23:30 | +15 | BNB | UP | 0.59 | open |  |
