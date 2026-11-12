# Range-Scalp Bot

*Updated Thu Nov 12 14:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57000 | 49686 | 7314 (101) | 7 | $-15695.10 | -4.4% |
| **+10¢** | 42598 | 34064 | 8534 (133) | 7 | $-14643.89 | -5.5% |
| **+15¢** | 35713 | 26529 | 9184 (167) | 7 | $-13246.36 | -5.9% |
| **+20¢** | 31816 | 22181 | 9635 (217) | 8 | $-11618.39 | -5.8% |
| **+10¢ (15¢ stop)** | 69511 | 69383 | 128 (78) | 3 | $-25704.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 14:06 | +10 stop | DOGE | DOWN | 0.54 | 0.67 | 0.96 |
| 11-12 14:05 | +10 stop | NEAR | UP | 0.66 | open |  |
| 11-12 14:05 | +10 | NEAR | UP | 0.66 | open |  |
| 11-12 14:05 | +5 | NEAR | UP | 0.69 | open |  |
| 11-12 14:05 | +10 stop | HYPE | DOWN | 0.62 | open |  |
| 11-12 14:05 | +20 | HYPE | DOWN | 0.62 | open |  |
| 11-12 14:05 | +15 | HYPE | DOWN | 0.62 | open |  |
| 11-12 14:05 | +10 | HYPE | DOWN | 0.62 | open |  |
| 11-12 14:05 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-12 14:05 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 11-12 14:04 | +10 stop | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-12 14:04 | +10 stop | DOGE | DOWN | 0.70 | 0.52 | -2.13 |
| 11-12 14:04 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-12 14:04 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-12 14:04 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-12 14:04 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-12 14:04 | +10 stop | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-12 14:03 | +10 stop | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 11-12 14:03 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 11-12 14:03 | +5 | SOL | DOWN | 0.69 | open |  |
| 11-12 14:03 | +10 stop | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-12 14:03 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-12 14:03 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-12 14:03 | +10 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-12 14:03 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 11-12 14:02 | +10 stop | BNB | DOWN | 0.65 | 0.49 | -1.94 |
| 11-12 14:02 | +10 stop | NEAR | DOWN | 0.61 | 0.38 | -2.64 |
| 11-12 14:02 | +5 | ZEC | DOWN | 0.60 | open |  |
| 11-12 14:02 | +10 stop | SOL | DOWN | 0.68 | 0.51 | -2.04 |
| 11-12 14:02 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-12 14:02 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-12 14:02 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-12 14:02 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.30 |
| 11-12 14:01 | +10 stop | ETH | UP | 0.56 | 0.41 | -1.85 |
| 11-12 14:01 | +20 | ETH | UP | 0.56 | open |  |
| 11-12 14:01 | +15 | ETH | UP | 0.56 | open |  |
| 11-12 14:01 | +10 | ETH | UP | 0.56 | open |  |
| 11-12 14:01 | +5 | ETH | UP | 0.57 | open |  |
| 11-12 14:01 | +10 stop | BNB | UP | 0.57 | 0.39 | -2.15 |
| 11-12 14:01 | +20 | BNB | UP | 0.57 | open |  |
