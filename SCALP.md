# Range-Scalp Bot

*Updated Thu Oct 22 21:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29276 | 25487 | 3789 (39) | 8 | $-8597.49 | -4.7% |
| **+10¢** | 21960 | 17574 | 4386 (55) | 9 | $-7734.18 | -5.6% |
| **+15¢** | 18384 | 13672 | 4712 (78) | 9 | $-6928.69 | -6.0% |
| **+20¢** | 16273 | 11332 | 4941 (100) | 9 | $-6271.70 | -6.1% |
| **+10¢ (15¢ stop)** | 35931 | 35872 | 59 (32) | 8 | $-13544.07 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 21:03 | +5 | SOL | DOWN | 0.57 | open |  |
| 10-22 21:03 | +10 stop | ETH | DOWN | 0.58 | open |  |
| 10-22 21:03 | +10 | ETH | DOWN | 0.58 | open |  |
| 10-22 21:03 | +5 | ETH | DOWN | 0.58 | open |  |
| 10-22 21:02 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 10-22 21:02 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 10-22 21:01 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-22 21:01 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-22 21:01 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-22 21:01 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-22 21:01 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-22 21:01 | +10 stop | DOGE | UP | 0.65 | open |  |
| 10-22 21:01 | +20 | DOGE | UP | 0.65 | open |  |
| 10-22 21:01 | +15 | DOGE | UP | 0.65 | open |  |
| 10-22 21:01 | +10 | DOGE | UP | 0.65 | open |  |
| 10-22 21:01 | +5 | DOGE | UP | 0.65 | open |  |
| 10-22 21:01 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 10-22 21:01 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-22 21:01 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-22 21:01 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-22 21:01 | +5 | BNB | DOWN | 0.66 | open |  |
| 10-22 21:01 | +10 stop | HYPE | UP | 0.57 | open |  |
| 10-22 21:01 | +20 | HYPE | UP | 0.56 | open |  |
| 10-22 21:01 | +15 | HYPE | UP | 0.57 | open |  |
| 10-22 21:01 | +10 | HYPE | UP | 0.58 | open |  |
| 10-22 21:01 | +5 | HYPE | UP | 0.58 | 0.66 | 0.46 |
| 10-22 21:01 | +10 stop | XRP | UP | 0.64 | open |  |
| 10-22 21:01 | +20 | XRP | UP | 0.66 | open |  |
| 10-22 21:01 | +15 | XRP | UP | 0.66 | open |  |
| 10-22 21:01 | +10 | XRP | UP | 0.66 | open |  |
| 10-22 21:01 | +5 | XRP | UP | 0.66 | open |  |
| 10-22 21:01 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 10-22 21:01 | +20 | BTC | UP | 0.57 | open |  |
| 10-22 21:01 | +15 | BTC | UP | 0.57 | open |  |
| 10-22 21:01 | +10 | BTC | UP | 0.57 | open |  |
| 10-22 21:01 | +5 | BTC | UP | 0.58 | open |  |
| 10-22 21:01 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 21:01 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-22 21:01 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-22 21:01 | +10 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
