# Range-Scalp Bot

*Updated Sun Oct 11 17:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12233 | 10550 | 1683 (24) | 6 | $-4103.88 | -5.3% |
| **+10¢** | 9292 | 7340 | 1952 (37) | 7 | $-3875.42 | -6.6% |
| **+15¢** | 7830 | 5758 | 2072 (54) | 7 | $-3315.43 | -6.7% |
| **+20¢** | 6978 | 4819 | 2159 (68) | 7 | $-2816.80 | -6.4% |
| **+10¢ (15¢ stop)** | 15064 | 15023 | 41 (25) | 5 | $-5938.76 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 17:35 | +10 stop | ETH | UP | 0.63 | open |  |
| 10-11 17:35 | +5 | ETH | UP | 0.63 | open |  |
| 10-11 17:34 | +10 stop | DOGE | UP | 0.70 | open |  |
| 10-11 17:34 | +10 | DOGE | UP | 0.70 | open |  |
| 10-11 17:34 | +5 | DOGE | UP | 0.70 | open |  |
| 10-11 17:34 | +10 stop | BTC | UP | 0.71 | open |  |
| 10-11 17:34 | +5 | ETH | DOWN | 0.53 | 0.64 | 0.75 |
| 10-11 17:34 | +10 stop | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 17:34 | +10 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 17:34 | +5 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 17:33 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-11 17:33 | +5 | HYPE | UP | 0.62 | 0.71 | 0.58 |
| 10-11 17:32 | +5 | HYPE | DOWN | 0.50 | 0.55 | 0.14 |
| 10-11 17:32 | +5 | XRP | DOWN | 0.61 | open |  |
| 10-11 17:32 | +10 stop | DOGE | UP | 0.54 | 0.67 | 0.96 |
| 10-11 17:32 | +10 | DOGE | UP | 0.54 | 0.67 | 0.96 |
| 10-11 17:32 | +5 | DOGE | UP | 0.54 | 0.62 | 0.45 |
| 10-11 17:32 | +10 stop | NEAR | UP | 0.56 | open |  |
| 10-11 17:32 | +20 | NEAR | UP | 0.56 | open |  |
| 10-11 17:32 | +15 | NEAR | UP | 0.56 | open |  |
| 10-11 17:32 | +10 | NEAR | UP | 0.56 | open |  |
| 10-11 17:32 | +5 | NEAR | UP | 0.56 | open |  |
| 10-11 17:31 | +10 stop | XRP | DOWN | 0.56 | 0.23 | -3.61 |
| 10-11 17:31 | +20 | XRP | DOWN | 0.56 | open |  |
| 10-11 17:31 | +15 | XRP | DOWN | 0.56 | open |  |
| 10-11 17:31 | +10 | XRP | DOWN | 0.56 | open |  |
| 10-11 17:31 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.35 |
| 10-11 17:31 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.82 |
| 10-11 17:31 | +20 | SOL | UP | 0.63 | 0.85 | 1.97 |
| 10-11 17:31 | +15 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 10-11 17:31 | +10 | SOL | UP | 0.62 | 0.74 | 0.89 |
| 10-11 17:31 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 10-11 17:31 | +10 stop | DOGE | DOWN | 0.42 | 0.54 | 0.84 |
| 10-11 17:31 | +20 | DOGE | DOWN | 0.42 | open |  |
| 10-11 17:31 | +15 | DOGE | DOWN | 0.42 | open |  |
| 10-11 17:31 | +10 | DOGE | DOWN | 0.42 | 0.54 | 0.84 |
| 10-11 17:31 | +5 | DOGE | DOWN | 0.42 | 0.54 | 0.84 |
| 10-11 17:31 | +10 stop | ETH | DOWN | 0.55 | 0.40 | -1.85 |
| 10-11 17:31 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-11 17:31 | +15 | ETH | DOWN | 0.55 | open |  |
