# Range-Scalp Bot

*Updated Sat Nov 07 08:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50761 | 44254 | 6507 (76) | 6 | $-14212.34 | -4.4% |
| **+10¢** | 37892 | 30310 | 7582 (102) | 7 | $-13174.40 | -5.5% |
| **+15¢** | 31718 | 23550 | 8168 (131) | 7 | $-12077.19 | -6.1% |
| **+20¢** | 28202 | 19640 | 8562 (173) | 8 | $-10668.86 | -6.0% |
| **+10¢ (15¢ stop)** | 61812 | 61713 | 99 (58) | 6 | $-22861.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 08:32 | +10 stop | BTC | DOWN | 0.56 | open |  |
| 11-07 08:32 | +20 | BTC | DOWN | 0.56 | open |  |
| 11-07 08:32 | +15 | BTC | DOWN | 0.56 | open |  |
| 11-07 08:32 | +10 | BTC | DOWN | 0.56 | open |  |
| 11-07 08:32 | +5 | BTC | DOWN | 0.56 | open |  |
| 11-07 08:32 | +10 stop | NEAR | UP | 0.55 | open |  |
| 11-07 08:32 | +20 | NEAR | UP | 0.55 | open |  |
| 11-07 08:32 | +15 | NEAR | UP | 0.55 | open |  |
| 11-07 08:32 | +10 | NEAR | UP | 0.55 | open |  |
| 11-07 08:32 | +5 | NEAR | UP | 0.55 | 0.61 | 0.25 |
| 11-07 08:32 | +10 stop | BNB | UP | 0.56 | open |  |
| 11-07 08:32 | +20 | BNB | UP | 0.56 | open |  |
| 11-07 08:32 | +15 | BNB | UP | 0.56 | open |  |
| 11-07 08:32 | +10 | BNB | UP | 0.56 | open |  |
| 11-07 08:32 | +5 | BNB | UP | 0.56 | open |  |
| 11-07 08:31 | +10 stop | HYPE | DOWN | 0.65 | 0.45 | -2.34 |
| 11-07 08:31 | +20 | HYPE | DOWN | 0.65 | open |  |
| 11-07 08:31 | +15 | HYPE | DOWN | 0.65 | open |  |
| 11-07 08:31 | +10 | HYPE | DOWN | 0.65 | open |  |
| 11-07 08:31 | +5 | HYPE | DOWN | 0.65 | open |  |
| 11-07 08:31 | +10 stop | XRP | UP | 0.54 | open |  |
| 11-07 08:31 | +20 | XRP | UP | 0.54 | open |  |
| 11-07 08:31 | +15 | XRP | UP | 0.54 | open |  |
| 11-07 08:31 | +10 | XRP | UP | 0.54 | open |  |
| 11-07 08:31 | +5 | XRP | UP | 0.54 | open |  |
| 11-07 08:31 | +10 stop | DOGE | UP | 0.64 | open |  |
| 11-07 08:31 | +20 | DOGE | UP | 0.64 | open |  |
| 11-07 08:31 | +15 | DOGE | UP | 0.64 | open |  |
| 11-07 08:31 | +10 | DOGE | UP | 0.63 | open |  |
| 11-07 08:31 | +5 | DOGE | UP | 0.63 | open |  |
| 11-07 08:31 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-07 08:31 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-07 08:31 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-07 08:31 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-07 08:31 | +5 | ZEC | DOWN | 0.68 | open |  |
| 11-07 08:31 | +10 stop | SOL | UP | 0.58 | 0.73 | 1.18 |
| 11-07 08:31 | +20 | SOL | UP | 0.58 | open |  |
| 11-07 08:31 | +15 | SOL | UP | 0.58 | 0.73 | 1.18 |
| 11-07 08:31 | +10 | SOL | UP | 0.58 | 0.73 | 1.18 |
| 11-07 08:31 | +5 | SOL | UP | 0.58 | 0.65 | 0.36 |
