# Range-Scalp Bot

*Updated Sun Oct 25 23:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33910 | 29608 | 4302 (43) | 7 | $-9365.97 | -4.4% |
| **+10¢** | 25383 | 20409 | 4974 (65) | 7 | $-8191.75 | -5.1% |
| **+15¢** | 21233 | 15879 | 5354 (89) | 7 | $-7309.67 | -5.5% |
| **+20¢** | 18815 | 13209 | 5606 (111) | 7 | $-6385.98 | -5.4% |
| **+10¢ (15¢ stop)** | 41541 | 41479 | 62 (33) | 0 | $-15792.72 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 23:34 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-25 23:34 | +20 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 10-25 23:34 | +15 | NEAR | UP | 0.68 | 0.83 | 1.24 |
| 10-25 23:34 | +10 | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-25 23:34 | +5 | NEAR | UP | 0.68 | 0.77 | 0.61 |
| 10-25 23:34 | +10 stop | BTC | UP | 0.70 | 0.85 | 1.26 |
| 10-25 23:33 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
| 10-25 23:33 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-25 23:33 | +15 | DOGE | DOWN | 0.59 | open |  |
| 10-25 23:33 | +10 | DOGE | DOWN | 0.59 | open |  |
| 10-25 23:33 | +5 | DOGE | DOWN | 0.59 | open |  |
| 10-25 23:33 | +10 stop | BNB | DOWN | 0.57 | 0.34 | -2.64 |
| 10-25 23:33 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-25 23:33 | +15 | BNB | DOWN | 0.59 | open |  |
| 10-25 23:33 | +10 | BNB | DOWN | 0.59 | open |  |
| 10-25 23:33 | +5 | BNB | DOWN | 0.59 | open |  |
| 10-25 23:33 | +10 stop | ETH | DOWN | 0.63 | 0.43 | -2.35 |
| 10-25 23:33 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-25 23:33 | +15 | ETH | DOWN | 0.63 | open |  |
| 10-25 23:33 | +10 | ETH | DOWN | 0.63 | open |  |
| 10-25 23:33 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-25 23:33 | +15 | HYPE | DOWN | 0.64 | open |  |
| 10-25 23:33 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-25 23:33 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-25 23:33 | +10 stop | HYPE | DOWN | 0.70 | 0.51 | -2.23 |
| 10-25 23:33 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-25 23:33 | +10 stop | SOL | DOWN | 0.65 | 0.46 | -2.24 |
| 10-25 23:33 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-25 23:33 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-25 23:33 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-25 23:33 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-25 23:32 | +10 stop | XRP | DOWN | 0.67 | 0.46 | -2.44 |
| 10-25 23:32 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-25 23:32 | +15 | XRP | DOWN | 0.67 | open |  |
| 10-25 23:32 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-25 23:32 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-25 23:32 | +10 stop | BTC | DOWN | 0.63 | 0.45 | -2.15 |
| 10-25 23:32 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-25 23:32 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-25 23:32 | +10 | BTC | DOWN | 0.58 | open |  |
