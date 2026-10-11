# Range-Scalp Bot

*Updated Sun Oct 11 19:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12333 | 10639 | 1694 (25) | 1 | $-4107.34 | -5.3% |
| **+10¢** | 9368 | 7408 | 1960 (37) | 2 | $-3853.80 | -6.5% |
| **+15¢** | 7894 | 5813 | 2081 (54) | 2 | $-3281.73 | -6.6% |
| **+20¢** | 7035 | 4866 | 2169 (68) | 6 | $-2777.61 | -6.3% |
| **+10¢ (15¢ stop)** | 15204 | 15163 | 41 (25) | 1 | $-5994.81 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 19:05 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 10-11 19:03 | +10 stop | ZEC | UP | 0.63 | 0.46 | -2.05 |
| 10-11 19:03 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 10-11 19:02 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 10-11 19:01 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-11 19:01 | +20 | DOGE | UP | 0.62 | 0.84 | 1.93 |
| 10-11 19:01 | +15 | DOGE | UP | 0.62 | 0.78 | 1.30 |
| 10-11 19:01 | +10 | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-11 19:01 | +5 | DOGE | UP | 0.62 | 0.69 | 0.38 |
| 10-11 19:01 | +10 stop | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-11 19:01 | +20 | BNB | UP | 0.58 | 0.82 | 2.11 |
| 10-11 19:01 | +15 | BNB | UP | 0.58 | 0.74 | 1.28 |
| 10-11 19:01 | +10 | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-11 19:01 | +5 | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-11 19:01 | +10 stop | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 10-11 19:01 | +20 | HYPE | UP | 0.69 | 0.89 | 1.78 |
| 10-11 19:01 | +15 | HYPE | UP | 0.69 | 0.87 | 1.57 |
| 10-11 19:01 | +10 | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 10-11 19:01 | +5 | HYPE | UP | 0.69 | 0.77 | 0.52 |
| 10-11 19:01 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-11 19:01 | +20 | BTC | UP | 0.64 | open |  |
| 10-11 19:01 | +15 | BTC | UP | 0.64 | 0.79 | 1.21 |
| 10-11 19:01 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-11 19:01 | +5 | BTC | UP | 0.64 | 0.70 | 0.28 |
| 10-11 19:01 | +10 stop | ZEC | DOWN | 0.56 | 0.38 | -2.13 |
| 10-11 19:01 | +20 | ZEC | DOWN | 0.55 | open |  |
| 10-11 19:01 | +15 | ZEC | DOWN | 0.58 | open |  |
| 10-11 19:01 | +10 | ZEC | DOWN | 0.57 | open |  |
| 10-11 19:01 | +5 | ZEC | DOWN | 0.56 | 0.64 | 0.47 |
| 10-11 19:01 | +10 stop | SOL | UP | 0.62 | 0.74 | 0.89 |
| 10-11 19:01 | +20 | SOL | UP | 0.62 | open |  |
| 10-11 19:01 | +15 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-11 19:01 | +10 | SOL | UP | 0.62 | 0.74 | 0.89 |
| 10-11 19:01 | +5 | SOL | UP | 0.62 | 0.74 | 0.89 |
| 10-11 19:01 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-11 19:01 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 10-11 19:01 | +20 | XRP | UP | 0.65 | open |  |
| 10-11 19:01 | +15 | XRP | UP | 0.65 | 0.81 | 1.33 |
| 10-11 19:01 | +10 | XRP | UP | 0.65 | 0.75 | 0.70 |
| 10-11 19:01 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
