# Range-Scalp Bot

*Updated Fri Oct 30 23:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41403 | 36134 | 5269 (54) | 6 | $-11570.65 | -4.4% |
| **+10¢** | 30860 | 24763 | 6097 (78) | 7 | $-10308.00 | -5.3% |
| **+15¢** | 25796 | 19225 | 6571 (106) | 7 | $-9375.38 | -5.8% |
| **+20¢** | 22898 | 16016 | 6882 (137) | 7 | $-8248.61 | -5.7% |
| **+10¢ (15¢ stop)** | 50458 | 50383 | 75 (41) | 7 | $-19062.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 23:17 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 10-30 23:17 | +20 | BTC | DOWN | 0.70 | open |  |
| 10-30 23:17 | +15 | BTC | DOWN | 0.70 | open |  |
| 10-30 23:17 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-30 23:17 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-30 23:17 | +5 | NEAR | UP | 0.67 | open |  |
| 10-30 23:16 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 10-30 23:16 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-30 23:16 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-30 23:16 | +10 | ZEC | DOWN | 0.61 | open |  |
| 10-30 23:16 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-30 23:16 | +10 stop | NEAR | UP | 0.60 | open |  |
| 10-30 23:16 | +20 | NEAR | UP | 0.60 | open |  |
| 10-30 23:16 | +15 | NEAR | UP | 0.60 | open |  |
| 10-30 23:16 | +10 | NEAR | UP | 0.60 | open |  |
| 10-30 23:16 | +5 | NEAR | UP | 0.60 | 0.66 | 0.27 |
| 10-30 23:16 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-30 23:16 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-30 23:16 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-30 23:16 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-30 23:16 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-30 23:16 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-30 23:16 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-30 23:16 | +15 | HYPE | DOWN | 0.71 | open |  |
| 10-30 23:16 | +10 | HYPE | DOWN | 0.71 | open |  |
| 10-30 23:16 | +5 | HYPE | DOWN | 0.71 | open |  |
| 10-30 23:16 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 10-30 23:16 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-30 23:16 | +15 | SOL | DOWN | 0.64 | open |  |
| 10-30 23:16 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-30 23:16 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-30 23:16 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-30 23:16 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-30 23:16 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-30 23:16 | +10 | ETH | DOWN | 0.69 | open |  |
| 10-30 23:16 | +5 | ETH | DOWN | 0.69 | open |  |
| 10-30 23:13 | +10 stop | HYPE | DOWN | 0.54 | 0.26 | -3.11 |
| 10-30 23:13 | +20 | HYPE | DOWN | 0.51 | yes | -5.28 |
| 10-30 23:13 | +15 | HYPE | DOWN | 0.51 | yes | -5.28 |
| 10-30 23:13 | +10 | HYPE | DOWN | 0.51 | 0.61 | 0.65 |
