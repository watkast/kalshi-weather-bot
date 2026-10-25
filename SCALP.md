# Range-Scalp Bot

*Updated Sun Oct 25 20:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33718 | 29432 | 4286 (43) | 4 | $-9376.02 | -4.4% |
| **+10¢** | 25229 | 20271 | 4958 (65) | 6 | $-8259.52 | -5.2% |
| **+15¢** | 21102 | 15766 | 5336 (89) | 6 | $-7377.61 | -5.6% |
| **+20¢** | 18701 | 13114 | 5587 (111) | 6 | $-6466.51 | -5.5% |
| **+10¢ (15¢ stop)** | 41286 | 41224 | 62 (33) | 5 | $-15712.80 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 20:31 | +5 | HYPE | UP | 0.54 | 0.60 | 0.25 |
| 10-25 20:31 | +10 stop | HYPE | UP | 0.51 | open |  |
| 10-25 20:31 | +20 | HYPE | UP | 0.51 | open |  |
| 10-25 20:31 | +15 | HYPE | UP | 0.51 | open |  |
| 10-25 20:31 | +10 | HYPE | UP | 0.51 | open |  |
| 10-25 20:31 | +5 | HYPE | UP | 0.51 | 0.57 | 0.24 |
| 10-25 20:30 | +10 stop | BNB | UP | 0.61 | open |  |
| 10-25 20:30 | +20 | BNB | UP | 0.61 | open |  |
| 10-25 20:30 | +15 | BNB | UP | 0.61 | open |  |
| 10-25 20:30 | +10 | BNB | UP | 0.61 | open |  |
| 10-25 20:30 | +5 | BNB | UP | 0.61 | 0.70 | 0.58 |
| 10-25 20:30 | +10 stop | ZEC | UP | 0.65 | 0.45 | -2.34 |
| 10-25 20:30 | +20 | ZEC | UP | 0.65 | open |  |
| 10-25 20:30 | +15 | ZEC | UP | 0.65 | open |  |
| 10-25 20:30 | +10 | ZEC | UP | 0.65 | open |  |
| 10-25 20:30 | +5 | ZEC | UP | 0.64 | open |  |
| 10-25 20:30 | +10 stop | DOGE | UP | 0.62 | open |  |
| 10-25 20:30 | +20 | DOGE | UP | 0.62 | open |  |
| 10-25 20:30 | +15 | DOGE | UP | 0.62 | open |  |
| 10-25 20:30 | +10 | DOGE | UP | 0.62 | open |  |
| 10-25 20:30 | +5 | DOGE | UP | 0.62 | open |  |
| 10-25 20:30 | +10 stop | ETH | UP | 0.63 | open |  |
| 10-25 20:30 | +20 | ETH | UP | 0.63 | open |  |
| 10-25 20:30 | +15 | ETH | UP | 0.63 | open |  |
| 10-25 20:30 | +10 | ETH | UP | 0.63 | open |  |
| 10-25 20:30 | +5 | ETH | UP | 0.64 | open |  |
| 10-25 20:30 | +10 stop | XRP | UP | 0.64 | open |  |
| 10-25 20:30 | +20 | XRP | UP | 0.64 | open |  |
| 10-25 20:30 | +15 | XRP | UP | 0.64 | open |  |
| 10-25 20:30 | +10 | XRP | UP | 0.64 | open |  |
| 10-25 20:30 | +5 | XRP | UP | 0.64 | open |  |
| 10-25 20:26 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-25 20:25 | +10 stop | ZEC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-25 20:25 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-25 20:25 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-25 20:25 | +10 stop | DOGE | UP | 0.64 | 0.46 | -2.15 |
| 10-25 20:25 | +10 | DOGE | UP | 0.64 | no | -6.57 |
| 10-25 20:25 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-25 20:24 | +10 stop | XRP | UP | 0.38 | 0.59 | 1.76 |
| 10-25 20:23 | +10 stop | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
