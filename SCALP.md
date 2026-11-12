# Range-Scalp Bot

*Updated Thu Nov 12 13:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56988 | 49680 | 7308 (101) | 7 | $-15659.55 | -4.4% |
| **+10¢** | 42587 | 34060 | 8527 (133) | 7 | $-14601.30 | -5.5% |
| **+15¢** | 35704 | 26527 | 9177 (167) | 7 | $-13202.82 | -5.9% |
| **+20¢** | 31808 | 22180 | 9628 (217) | 7 | $-11575.38 | -5.8% |
| **+10¢ (15¢ stop)** | 69494 | 69366 | 128 (78) | 2 | $-25691.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 13:56 | +10 stop | XRP | UP | 0.60 | open |  |
| 11-12 13:55 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 11-12 13:54 | +10 stop | XRP | DOWN | 0.68 | 0.51 | -2.04 |
| 11-12 13:54 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-12 13:52 | +10 stop | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-12 13:52 | +15 | NEAR | DOWN | 0.62 | 0.90 | 2.58 |
| 11-12 13:52 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-12 13:52 | +10 stop | XRP | UP | 0.56 | 0.67 | 0.76 |
| 11-12 13:51 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-12 13:51 | +10 | NEAR | DOWN | 0.69 | 0.90 | 1.90 |
| 11-12 13:51 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.76 |
| 11-12 13:51 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.22 |
| 11-12 13:51 | +5 | NEAR | DOWN | 0.69 | 0.90 | 1.90 |
| 11-12 13:50 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 13:50 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 13:50 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 13:50 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.06 |
| 11-12 13:50 | +10 stop | XRP | UP | 0.66 | 0.45 | -2.39 |
| 11-12 13:50 | +20 | XRP | UP | 0.66 | open |  |
| 11-12 13:50 | +15 | XRP | UP | 0.64 | open |  |
| 11-12 13:50 | +10 | XRP | UP | 0.64 | open |  |
| 11-12 13:50 | +5 | XRP | UP | 0.64 | 0.69 | 0.19 |
| 11-12 13:50 | +10 stop | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-12 13:50 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.09 |
| 11-12 13:50 | +10 stop | ZEC | UP | 0.57 | 0.30 | -3.03 |
| 11-12 13:50 | +20 | ZEC | UP | 0.57 | open |  |
| 11-12 13:50 | +15 | ZEC | UP | 0.57 | open |  |
| 11-12 13:50 | +10 | ZEC | UP | 0.57 | open |  |
| 11-12 13:50 | +5 | ZEC | UP | 0.58 | open |  |
| 11-12 13:50 | +10 stop | NEAR | DOWN | 0.68 | 0.90 | 1.99 |
| 11-12 13:49 | +10 | ETH | UP | 0.63 | open |  |
| 11-12 13:49 | +5 | ETH | UP | 0.62 | open |  |
| 11-12 13:49 | +10 stop | BNB | UP | 0.65 | 0.40 | -2.86 |
| 11-12 13:49 | +15 | BNB | UP | 0.65 | open |  |
| 11-12 13:49 | +10 | BNB | UP | 0.65 | open |  |
| 11-12 13:49 | +5 | BNB | UP | 0.65 | open |  |
| 11-12 13:49 | +5 | DOGE | UP | 0.67 | open |  |
| 11-12 13:49 | +10 stop | BTC | UP | 0.68 | 0.48 | -2.34 |
| 11-12 13:49 | +10 stop | NEAR | UP | 0.71 | 0.54 | -2.03 |
| 11-12 13:48 | +10 stop | SOL | UP | 0.68 | 0.52 | -1.92 |
