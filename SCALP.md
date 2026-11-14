# Range-Scalp Bot

*Updated Sat Nov 14 22:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59956 | 52295 | 7661 (107) | 1 | $-16347.92 | -4.3% |
| **+10¢** | 44800 | 35827 | 8973 (143) | 3 | $-15414.05 | -5.5% |
| **+15¢** | 37534 | 27859 | 9675 (180) | 3 | $-14060.85 | -6.0% |
| **+20¢** | 33439 | 23289 | 10150 (232) | 3 | $-12403.65 | -5.9% |
| **+10¢ (15¢ stop)** | 72987 | 72844 | 143 (82) | 0 | $-26819.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 22:34 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-14 22:34 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-14 22:34 | +5 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-14 22:33 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-14 22:32 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 22:32 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-14 22:32 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 22:32 | +20 | XRP | DOWN | 0.69 | 0.90 | 1.89 |
| 11-14 22:32 | +15 | XRP | DOWN | 0.69 | 0.88 | 1.67 |
| 11-14 22:32 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 22:32 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-14 22:32 | +10 stop | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-14 22:32 | +20 | BTC | DOWN | 0.70 | 0.90 | 1.81 |
| 11-14 22:32 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-14 22:32 | +10 | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-14 22:32 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-14 22:32 | +5 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-14 22:32 | +10 stop | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 11-14 22:32 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.90 |
| 11-14 22:32 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-14 22:32 | +10 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 11-14 22:32 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-14 22:31 | +10 stop | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-14 22:31 | +20 | NEAR | DOWN | 0.55 | 0.76 | 1.79 |
| 11-14 22:31 | +15 | NEAR | DOWN | 0.55 | 0.72 | 1.37 |
| 11-14 22:31 | +10 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-14 22:31 | +5 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-14 22:31 | +10 stop | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-14 22:31 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-14 22:31 | +15 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-14 22:31 | +10 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-14 22:31 | +5 | ZEC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-14 22:31 | +10 stop | ETH | UP | 0.52 | 0.33 | -2.24 |
| 11-14 22:31 | +20 | ETH | UP | 0.52 | open |  |
| 11-14 22:31 | +15 | ETH | UP | 0.53 | open |  |
| 11-14 22:31 | +10 | ETH | UP | 0.52 | open |  |
| 11-14 22:31 | +5 | ETH | UP | 0.52 | open |  |
| 11-14 22:31 | +10 stop | DOGE | UP | 0.58 | 0.34 | -2.74 |
| 11-14 22:31 | +20 | DOGE | UP | 0.59 | open |  |
| 11-14 22:31 | +15 | DOGE | UP | 0.59 | open |  |
