# Range-Scalp Bot

*Updated Fri Oct 16 12:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19206 | 16683 | 2523 (29) | 5 | $-5830.59 | -4.8% |
| **+10¢** | 14480 | 11563 | 2917 (41) | 7 | $-5271.72 | -5.8% |
| **+15¢** | 12123 | 8984 | 3139 (60) | 8 | $-4779.03 | -6.3% |
| **+20¢** | 10757 | 7466 | 3291 (79) | 8 | $-4265.00 | -6.3% |
| **+10¢ (15¢ stop)** | 23625 | 23575 | 50 (29) | 6 | $-9109.22 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 12:32 | +10 stop | HYPE | DOWN | 0.51 | open |  |
| 10-16 12:32 | +20 | HYPE | DOWN | 0.51 | open |  |
| 10-16 12:32 | +15 | HYPE | DOWN | 0.51 | open |  |
| 10-16 12:32 | +10 | HYPE | DOWN | 0.51 | open |  |
| 10-16 12:32 | +5 | HYPE | DOWN | 0.51 | 0.57 | 0.24 |
| 10-16 12:32 | +10 stop | ZEC | UP | 0.56 | 0.69 | 0.97 |
| 10-16 12:32 | +20 | ZEC | UP | 0.56 | open |  |
| 10-16 12:32 | +15 | ZEC | UP | 0.56 | open |  |
| 10-16 12:32 | +10 | ZEC | UP | 0.56 | 0.69 | 0.97 |
| 10-16 12:32 | +5 | ZEC | UP | 0.56 | 0.69 | 0.97 |
| 10-16 12:32 | +10 stop | BNB | UP | 0.62 | open |  |
| 10-16 12:32 | +20 | BNB | UP | 0.62 | open |  |
| 10-16 12:32 | +15 | BNB | UP | 0.62 | open |  |
| 10-16 12:32 | +10 | BNB | UP | 0.62 | open |  |
| 10-16 12:32 | +5 | BNB | UP | 0.62 | open |  |
| 10-16 12:32 | +10 stop | DOGE | UP | 0.71 | open |  |
| 10-16 12:32 | +20 | DOGE | UP | 0.71 | open |  |
| 10-16 12:32 | +15 | DOGE | UP | 0.71 | open |  |
| 10-16 12:32 | +10 | DOGE | UP | 0.71 | open |  |
| 10-16 12:32 | +5 | DOGE | UP | 0.71 | open |  |
| 10-16 12:32 | +10 stop | XRP | UP | 0.60 | open |  |
| 10-16 12:32 | +20 | XRP | UP | 0.60 | open |  |
| 10-16 12:32 | +15 | XRP | UP | 0.60 | open |  |
| 10-16 12:32 | +10 | XRP | UP | 0.60 | open |  |
| 10-16 12:32 | +5 | XRP | UP | 0.60 | open |  |
| 10-16 12:32 | +10 stop | SOL | UP | 0.58 | open |  |
| 10-16 12:32 | +20 | SOL | UP | 0.58 | open |  |
| 10-16 12:32 | +15 | SOL | UP | 0.58 | open |  |
| 10-16 12:32 | +10 | SOL | UP | 0.58 | open |  |
| 10-16 12:32 | +5 | SOL | UP | 0.57 | open |  |
| 10-16 12:31 | +10 stop | ETH | DOWN | 0.53 | open |  |
| 10-16 12:31 | +20 | ETH | DOWN | 0.53 | open |  |
| 10-16 12:31 | +15 | ETH | DOWN | 0.53 | open |  |
| 10-16 12:31 | +10 | ETH | DOWN | 0.53 | open |  |
| 10-16 12:31 | +5 | ETH | DOWN | 0.54 | 0.59 | 0.15 |
| 10-16 12:31 | +10 stop | BTC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-16 12:31 | +20 | BTC | DOWN | 0.63 | open |  |
| 10-16 12:31 | +15 | BTC | DOWN | 0.63 | open |  |
| 10-16 12:31 | +10 | BTC | DOWN | 0.63 | open |  |
| 10-16 12:31 | +5 | BTC | DOWN | 0.62 | open |  |
