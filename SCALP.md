# Range-Scalp Bot

*Updated Wed Oct 21 09:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26980 | 23490 | 3490 (39) | 6 | $-7869.58 | -4.6% |
| **+10¢** | 20294 | 16262 | 4032 (55) | 9 | $-6964.48 | -5.5% |
| **+15¢** | 16990 | 12652 | 4338 (78) | 9 | $-6229.63 | -5.8% |
| **+20¢** | 15045 | 10497 | 4548 (97) | 9 | $-5603.47 | -5.9% |
| **+10¢ (15¢ stop)** | 33088 | 33029 | 59 (32) | 9 | $-12251.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 09:32 | +5 | SOL | UP | 0.64 | open |  |
| 10-21 09:32 | +10 stop | DOGE | DOWN | 0.53 | open |  |
| 10-21 09:32 | +10 stop | NEAR | UP | 0.68 | open |  |
| 10-21 09:31 | +10 stop | SOL | DOWN | 0.52 | open |  |
| 10-21 09:31 | +20 | SOL | DOWN | 0.52 | open |  |
| 10-21 09:31 | +15 | SOL | DOWN | 0.52 | open |  |
| 10-21 09:31 | +10 | SOL | DOWN | 0.52 | open |  |
| 10-21 09:31 | +5 | SOL | DOWN | 0.52 | 0.58 | 0.24 |
| 10-21 09:31 | +5 | ZEC | UP | 0.61 | open |  |
| 10-21 09:31 | +10 stop | NEAR | DOWN | 0.64 | 0.37 | -3.04 |
| 10-21 09:31 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-21 09:31 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-21 09:31 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-21 09:31 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-21 09:31 | +10 stop | XRP | UP | 0.54 | open |  |
| 10-21 09:31 | +20 | XRP | UP | 0.55 | open |  |
| 10-21 09:31 | +15 | XRP | UP | 0.57 | open |  |
| 10-21 09:31 | +10 | XRP | UP | 0.57 | open |  |
| 10-21 09:31 | +5 | XRP | UP | 0.57 | open |  |
| 10-21 09:31 | +10 stop | BNB | UP | 0.54 | open |  |
| 10-21 09:31 | +20 | BNB | UP | 0.54 | open |  |
| 10-21 09:31 | +15 | BNB | UP | 0.54 | open |  |
| 10-21 09:31 | +10 | BNB | UP | 0.54 | open |  |
| 10-21 09:31 | +5 | BNB | UP | 0.54 | 0.59 | 0.15 |
| 10-21 09:31 | +10 stop | DOGE | UP | 0.53 | 0.38 | -1.85 |
| 10-21 09:31 | +20 | DOGE | UP | 0.53 | open |  |
| 10-21 09:31 | +15 | DOGE | UP | 0.53 | open |  |
| 10-21 09:31 | +10 | DOGE | UP | 0.53 | open |  |
| 10-21 09:31 | +5 | DOGE | UP | 0.53 | open |  |
| 10-21 09:31 | +10 stop | HYPE | UP | 0.65 | open |  |
| 10-21 09:31 | +20 | HYPE | UP | 0.65 | open |  |
| 10-21 09:31 | +15 | HYPE | UP | 0.65 | open |  |
| 10-21 09:31 | +10 | HYPE | UP | 0.65 | open |  |
| 10-21 09:31 | +5 | HYPE | UP | 0.65 | 0.70 | 0.22 |
| 10-21 09:31 | +10 stop | ETH | UP | 0.53 | open |  |
| 10-21 09:31 | +20 | ETH | UP | 0.53 | open |  |
| 10-21 09:31 | +15 | ETH | UP | 0.53 | open |  |
| 10-21 09:31 | +10 | ETH | UP | 0.53 | open |  |
| 10-21 09:31 | +5 | ETH | UP | 0.53 | 0.61 | 0.45 |
| 10-21 09:31 | +10 stop | ZEC | UP | 0.61 | open |  |
