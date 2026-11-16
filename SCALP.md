# Range-Scalp Bot

*Updated Mon Nov 16 21:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62234 | 54297 | 7937 (117) | 2 | $-16823.01 | -4.3% |
| **+10¢** | 46474 | 37187 | 9287 (159) | 2 | $-15685.56 | -5.4% |
| **+15¢** | 38943 | 28924 | 10019 (200) | 2 | $-14279.32 | -5.8% |
| **+20¢** | 34717 | 24211 | 10506 (255) | 2 | $-12446.25 | -5.7% |
| **+10¢ (15¢ stop)** | 75744 | 75588 | 156 (92) | 2 | $-27942.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 21:01 | +5 | NEAR | DOWN | 0.57 | open |  |
| 11-16 21:00 | +10 stop | ZEC | DOWN | 0.59 | open |  |
| 11-16 21:00 | +20 | ZEC | DOWN | 0.59 | open |  |
| 11-16 21:00 | +15 | ZEC | DOWN | 0.59 | open |  |
| 11-16 21:00 | +10 | ZEC | DOWN | 0.59 | open |  |
| 11-16 21:00 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-16 21:00 | +10 stop | NEAR | DOWN | 0.51 | open |  |
| 11-16 21:00 | +20 | NEAR | DOWN | 0.50 | open |  |
| 11-16 21:00 | +15 | NEAR | DOWN | 0.51 | open |  |
| 11-16 21:00 | +10 | NEAR | DOWN | 0.51 | open |  |
| 11-16 21:00 | +5 | NEAR | DOWN | 0.51 | 0.60 | 0.55 |
| 11-16 20:58 | +10 stop | BTC | DOWN | 0.23 | 0.57 | 3.09 |
| 11-16 20:58 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-16 20:58 | +5 | DOGE | DOWN | 0.64 | 0.72 | 0.48 |
| 11-16 20:58 | +10 stop | BTC | DOWN | 0.70 | 0.55 | -1.83 |
| 11-16 20:58 | +10 | BTC | DOWN | 0.68 | yes | -6.96 |
| 11-16 20:58 | +5 | BTC | DOWN | 0.67 | yes | -6.86 |
| 11-16 20:58 | +10 stop | ZEC | UP | 0.54 | 0.67 | 0.96 |
| 11-16 20:58 | +20 | ZEC | UP | 0.54 | 0.96 | 4.00 |
| 11-16 20:58 | +15 | ZEC | UP | 0.53 | 0.96 | 4.10 |
| 11-16 20:58 | +10 | ZEC | UP | 0.53 | 0.67 | 1.06 |
| 11-16 20:58 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 11-16 20:57 | +10 stop | ETH | UP | 0.61 | 0.93 | 2.97 |
| 11-16 20:57 | +20 | ETH | UP | 0.61 | 0.93 | 2.97 |
| 11-16 20:57 | +15 | ETH | UP | 0.62 | 0.93 | 2.87 |
| 11-16 20:57 | +10 | ETH | UP | 0.61 | 0.93 | 2.97 |
| 11-16 20:57 | +5 | ETH | UP | 0.62 | 0.93 | 2.87 |
| 11-16 20:57 | +10 stop | BTC | UP | 0.44 | 0.57 | 0.94 |
| 11-16 20:57 | +20 | BTC | UP | 0.44 | 0.85 | 3.83 |
| 11-16 20:57 | +15 | BTC | UP | 0.45 | 0.85 | 3.73 |
| 11-16 20:57 | +10 | BTC | UP | 0.45 | 0.57 | 0.84 |
| 11-16 20:57 | +5 | BTC | UP | 0.45 | 0.57 | 0.84 |
| 11-16 20:57 | +10 stop | DOGE | UP | 0.44 | 0.26 | -2.12 |
| 11-16 20:57 | +20 | DOGE | UP | 0.44 | no | -4.58 |
| 11-16 20:57 | +15 | DOGE | UP | 0.42 | no | -4.38 |
| 11-16 20:57 | +10 | DOGE | UP | 0.42 | 0.53 | 0.74 |
| 11-16 20:57 | +5 | DOGE | UP | 0.42 | 0.53 | 0.74 |
| 11-16 20:56 | +10 stop | XRP | UP | 0.65 | 0.28 | -4.01 |
| 11-16 20:56 | +20 | XRP | UP | 0.65 | 0.97 | 3.01 |
| 11-16 20:56 | +15 | XRP | UP | 0.65 | 0.97 | 3.01 |
