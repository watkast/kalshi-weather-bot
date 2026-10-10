# Range-Scalp Bot

*Updated Sat Oct 10 12:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10406 | 8972 | 1434 (22) | 6 | $-3546.60 | -5.4% |
| **+10¢** | 7877 | 6206 | 1671 (36) | 7 | $-3383.10 | -6.8% |
| **+15¢** | 6644 | 4872 | 1772 (52) | 7 | $-2867.14 | -6.9% |
| **+20¢** | 5907 | 4061 | 1846 (66) | 8 | $-2440.86 | -6.6% |
| **+10¢ (15¢ stop)** | 12784 | 12746 | 38 (25) | 7 | $-5009.18 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 12:32 | +10 stop | ZEC | UP | 0.66 | open |  |
| 10-10 12:32 | +20 | ZEC | UP | 0.66 | open |  |
| 10-10 12:32 | +15 | ZEC | UP | 0.66 | open |  |
| 10-10 12:32 | +10 | ZEC | UP | 0.66 | open |  |
| 10-10 12:32 | +5 | ZEC | UP | 0.66 | open |  |
| 10-10 12:32 | +5 | XRP | UP | 0.68 | open |  |
| 10-10 12:31 | +10 stop | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-10 12:31 | +20 | DOGE | UP | 0.61 | open |  |
| 10-10 12:31 | +15 | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-10 12:31 | +10 | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-10 12:31 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 10-10 12:31 | +10 stop | NEAR | DOWN | 0.59 | open |  |
| 10-10 12:31 | +20 | NEAR | DOWN | 0.59 | open |  |
| 10-10 12:31 | +15 | NEAR | DOWN | 0.59 | open |  |
| 10-10 12:31 | +10 | NEAR | DOWN | 0.59 | open |  |
| 10-10 12:31 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-10 12:31 | +10 stop | XRP | UP | 0.59 | open |  |
| 10-10 12:31 | +20 | XRP | UP | 0.59 | open |  |
| 10-10 12:31 | +15 | XRP | UP | 0.59 | open |  |
| 10-10 12:31 | +10 | XRP | UP | 0.59 | open |  |
| 10-10 12:31 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 10-10 12:31 | +10 stop | BTC | UP | 0.67 | open |  |
| 10-10 12:31 | +20 | BTC | UP | 0.67 | open |  |
| 10-10 12:31 | +15 | BTC | UP | 0.67 | open |  |
| 10-10 12:31 | +10 | BTC | UP | 0.67 | open |  |
| 10-10 12:31 | +5 | BTC | UP | 0.67 | open |  |
| 10-10 12:31 | +10 stop | BNB | UP | 0.51 | open |  |
| 10-10 12:31 | +20 | BNB | UP | 0.51 | open |  |
| 10-10 12:31 | +15 | BNB | UP | 0.51 | open |  |
| 10-10 12:31 | +10 | BNB | UP | 0.51 | open |  |
| 10-10 12:31 | +5 | BNB | UP | 0.51 | open |  |
| 10-10 12:31 | +10 stop | HYPE | UP | 0.61 | open |  |
| 10-10 12:31 | +20 | HYPE | UP | 0.61 | open |  |
| 10-10 12:31 | +15 | HYPE | UP | 0.61 | open |  |
| 10-10 12:31 | +10 | HYPE | UP | 0.61 | open |  |
| 10-10 12:31 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 10-10 12:31 | +10 stop | ETH | UP | 0.64 | open |  |
| 10-10 12:31 | +20 | ETH | UP | 0.64 | open |  |
| 10-10 12:31 | +15 | ETH | UP | 0.64 | open |  |
| 10-10 12:31 | +10 | ETH | UP | 0.64 | open |  |
