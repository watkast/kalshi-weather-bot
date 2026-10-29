# Range-Scalp Bot

*Updated Thu Oct 29 11:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39157 | 34167 | 4990 (49) | 4 | $-11010.85 | -4.5% |
| **+10¢** | 29207 | 23447 | 5760 (71) | 5 | $-9743.72 | -5.3% |
| **+15¢** | 24422 | 18234 | 6188 (98) | 7 | $-8709.83 | -5.7% |
| **+20¢** | 21667 | 15184 | 6483 (127) | 8 | $-7608.78 | -5.6% |
| **+10¢ (15¢ stop)** | 47865 | 47798 | 67 (35) | 3 | $-18162.05 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 11:03 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 10-29 11:03 | +10 | DOGE | DOWN | 0.65 | open |  |
| 10-29 11:03 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-29 11:02 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 11:02 | +20 | DOGE | DOWN | 0.61 | open |  |
| 10-29 11:02 | +15 | DOGE | DOWN | 0.61 | open |  |
| 10-29 11:02 | +10 | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 11:02 | +5 | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 11:02 | +10 stop | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 10-29 11:02 | +20 | HYPE | UP | 0.69 | open |  |
| 10-29 11:02 | +15 | HYPE | UP | 0.69 | open |  |
| 10-29 11:02 | +10 | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 10-29 11:02 | +5 | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 10-29 11:02 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-29 11:02 | +10 stop | XRP | DOWN | 0.71 | open |  |
| 10-29 11:02 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-29 11:02 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-29 11:02 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-29 11:02 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-29 11:02 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-29 11:02 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-29 11:02 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-29 11:02 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-29 11:02 | +10 stop | NEAR | UP | 0.53 | open |  |
| 10-29 11:02 | +20 | NEAR | UP | 0.53 | open |  |
| 10-29 11:02 | +15 | NEAR | UP | 0.53 | open |  |
| 10-29 11:02 | +10 | NEAR | UP | 0.53 | open |  |
| 10-29 11:02 | +5 | NEAR | UP | 0.53 | open |  |
| 10-29 11:01 | +10 stop | ZEC | UP | 0.43 | 0.61 | 1.45 |
| 10-29 11:01 | +20 | ZEC | UP | 0.43 | open |  |
| 10-29 11:01 | +15 | ZEC | UP | 0.44 | 0.61 | 1.35 |
| 10-29 11:01 | +10 | ZEC | UP | 0.44 | 0.61 | 1.35 |
| 10-29 11:01 | +5 | ZEC | UP | 0.44 | 0.61 | 1.35 |
| 10-29 11:01 | +10 stop | ETH | UP | 0.39 | 0.59 | 1.66 |
| 10-29 11:01 | +20 | ETH | UP | 0.39 | 0.59 | 1.66 |
| 10-29 11:01 | +15 | ETH | UP | 0.40 | 0.59 | 1.56 |
| 10-29 11:01 | +10 | ETH | UP | 0.40 | 0.59 | 1.56 |
| 10-29 11:01 | +5 | ETH | UP | 0.40 | 0.59 | 1.56 |
| 10-29 11:01 | +10 stop | BTC | UP | 0.68 | 0.39 | -3.23 |
| 10-29 11:01 | +20 | BTC | UP | 0.68 | open |  |
