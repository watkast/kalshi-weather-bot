# Range-Scalp Bot

*Updated Wed Oct 21 21:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27755 | 24173 | 3582 (39) | 7 | $-8050.25 | -4.6% |
| **+10¢** | 20859 | 16726 | 4133 (55) | 9 | $-7076.37 | -5.4% |
| **+15¢** | 17472 | 13025 | 4447 (78) | 9 | $-6308.93 | -5.8% |
| **+20¢** | 15468 | 10807 | 4661 (98) | 9 | $-5650.62 | -5.8% |
| **+10¢ (15¢ stop)** | 34066 | 34007 | 59 (32) | 8 | $-12663.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 21:33 | +10 stop | BNB | UP | 0.65 | open |  |
| 10-21 21:33 | +10 stop | BTC | UP | 0.55 | open |  |
| 10-21 21:32 | +10 stop | ETH | UP | 0.62 | open |  |
| 10-21 21:32 | +5 | XRP | DOWN | 0.55 | 0.64 | 0.55 |
| 10-21 21:32 | +10 stop | ZEC | UP | 0.62 | open |  |
| 10-21 21:32 | +20 | ZEC | UP | 0.62 | open |  |
| 10-21 21:32 | +15 | ZEC | UP | 0.62 | open |  |
| 10-21 21:32 | +10 | ZEC | UP | 0.62 | open |  |
| 10-21 21:32 | +5 | ZEC | UP | 0.62 | 0.67 | 0.19 |
| 10-21 21:32 | +5 | HYPE | UP | 0.57 | open |  |
| 10-21 21:32 | +10 stop | SOL | UP | 0.58 | open |  |
| 10-21 21:32 | +20 | SOL | UP | 0.58 | open |  |
| 10-21 21:32 | +15 | SOL | UP | 0.58 | open |  |
| 10-21 21:32 | +10 | SOL | UP | 0.59 | open |  |
| 10-21 21:32 | +5 | SOL | UP | 0.59 | open |  |
| 10-21 21:31 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 10-21 21:31 | +20 | DOGE | DOWN | 0.60 | open |  |
| 10-21 21:31 | +15 | DOGE | DOWN | 0.60 | open |  |
| 10-21 21:31 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-21 21:31 | +5 | DOGE | DOWN | 0.60 | open |  |
| 10-21 21:31 | +10 stop | BNB | DOWN | 0.61 | 0.43 | -2.15 |
| 10-21 21:31 | +20 | BNB | DOWN | 0.61 | open |  |
| 10-21 21:31 | +15 | BNB | DOWN | 0.61 | open |  |
| 10-21 21:31 | +10 | BNB | DOWN | 0.61 | open |  |
| 10-21 21:31 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-21 21:31 | +10 stop | NEAR | DOWN | 0.51 | 0.30 | -2.43 |
| 10-21 21:31 | +20 | NEAR | DOWN | 0.51 | open |  |
| 10-21 21:31 | +15 | NEAR | DOWN | 0.51 | open |  |
| 10-21 21:31 | +10 | NEAR | DOWN | 0.51 | open |  |
| 10-21 21:31 | +5 | NEAR | DOWN | 0.51 | open |  |
| 10-21 21:31 | +10 stop | ETH | DOWN | 0.58 | 0.42 | -1.96 |
| 10-21 21:31 | +20 | ETH | DOWN | 0.58 | open |  |
| 10-21 21:31 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-21 21:31 | +10 | ETH | DOWN | 0.58 | open |  |
| 10-21 21:31 | +5 | ETH | DOWN | 0.58 | open |  |
| 10-21 21:31 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-21 21:31 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-21 21:31 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-21 21:31 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-21 21:31 | +5 | BTC | DOWN | 0.59 | open |  |
