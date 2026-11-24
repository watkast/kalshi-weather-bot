# Range-Scalp Bot

*Updated Tue Nov 24 22:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71176 | 62128 | 9048 (155) | 3 | $-18961.82 | -4.2% |
| **+10¢** | 53086 | 42515 | 10571 (201) | 5 | $-17584.53 | -5.3% |
| **+15¢** | 44459 | 33078 | 11381 (258) | 8 | $-15635.67 | -5.6% |
| **+20¢** | 39582 | 27599 | 11983 (324) | 9 | $-14021.89 | -5.6% |
| **+10¢ (15¢ stop)** | 86649 | 86448 | 201 (121) | 4 | $-31856.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 22:18 | +5 | BNB | UP | 0.57 | 0.65 | 0.46 |
| 11-24 22:17 | +5 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-24 22:17 | +5 | SOL | UP | 0.66 | 0.74 | 0.50 |
| 11-24 22:17 | +5 | XRP | UP | 0.60 | 0.67 | 0.37 |
| 11-24 22:17 | +10 | NEAR | UP | 0.61 | open |  |
| 11-24 22:16 | +5 | NEAR | UP | 0.65 | open |  |
| 11-24 22:16 | +10 stop | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-24 22:16 | +20 | SOL | UP | 0.61 | open |  |
| 11-24 22:16 | +15 | SOL | UP | 0.61 | open |  |
| 11-24 22:16 | +10 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-24 22:16 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 11-24 22:16 | +10 stop | XRP | UP | 0.60 | 0.73 | 0.99 |
| 11-24 22:16 | +20 | XRP | UP | 0.60 | open |  |
| 11-24 22:16 | +15 | XRP | UP | 0.60 | 0.78 | 1.50 |
| 11-24 22:16 | +10 | XRP | UP | 0.60 | 0.73 | 0.99 |
| 11-24 22:16 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 11-24 22:16 | +10 stop | BNB | UP | 0.53 | 0.65 | 0.82 |
| 11-24 22:16 | +20 | BNB | UP | 0.55 | open |  |
| 11-24 22:16 | +15 | BNB | UP | 0.55 | open |  |
| 11-24 22:16 | +10 | BNB | UP | 0.55 | open |  |
| 11-24 22:16 | +5 | BNB | UP | 0.55 | 0.61 | 0.21 |
| 11-24 22:16 | +10 stop | ZEC | UP | 0.62 | open |  |
| 11-24 22:16 | +20 | ZEC | UP | 0.62 | open |  |
| 11-24 22:16 | +15 | ZEC | UP | 0.62 | open |  |
| 11-24 22:16 | +10 | ZEC | UP | 0.62 | open |  |
| 11-24 22:16 | +5 | ZEC | UP | 0.63 | 0.71 | 0.48 |
| 11-24 22:16 | +10 stop | HYPE | UP | 0.61 | open |  |
| 11-24 22:16 | +20 | HYPE | UP | 0.61 | open |  |
| 11-24 22:16 | +15 | HYPE | UP | 0.61 | open |  |
| 11-24 22:16 | +10 | HYPE | UP | 0.61 | open |  |
| 11-24 22:16 | +5 | HYPE | UP | 0.61 | open |  |
| 11-24 22:15 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-24 22:15 | +20 | BTC | UP | 0.65 | open |  |
| 11-24 22:15 | +15 | BTC | UP | 0.65 | open |  |
| 11-24 22:15 | +10 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-24 22:15 | +5 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-24 22:15 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 11-24 22:15 | +20 | ETH | UP | 0.69 | open |  |
| 11-24 22:15 | +15 | ETH | UP | 0.69 | open |  |
| 11-24 22:15 | +10 | ETH | UP | 0.69 | 0.81 | 0.94 |
