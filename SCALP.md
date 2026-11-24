# Range-Scalp Bot

*Updated Tue Nov 24 19:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70927 | 61909 | 9018 (155) | 2 | $-18895.36 | -4.2% |
| **+10¢** | 52903 | 42374 | 10529 (201) | 4 | $-17478.84 | -5.3% |
| **+15¢** | 44308 | 32966 | 11342 (258) | 6 | $-15575.11 | -5.6% |
| **+20¢** | 39449 | 27508 | 11941 (324) | 8 | $-13949.24 | -5.6% |
| **+10¢ (15¢ stop)** | 86337 | 86136 | 201 (121) | 4 | $-31721.50 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 19:04 | +5 | HYPE | UP | 0.53 | open |  |
| 11-24 19:03 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 11-24 19:03 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-24 19:03 | +5 | SOL | DOWN | 0.67 | 0.79 | 0.93 |
| 11-24 19:03 | +10 stop | HYPE | UP | 0.52 | open |  |
| 11-24 19:03 | +20 | HYPE | UP | 0.52 | open |  |
| 11-24 19:03 | +15 | HYPE | UP | 0.52 | open |  |
| 11-24 19:03 | +10 | HYPE | UP | 0.52 | open |  |
| 11-24 19:03 | +5 | HYPE | UP | 0.52 | 0.57 | 0.14 |
| 11-24 19:02 | +10 stop | BTC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-24 19:02 | +20 | BTC | DOWN | 0.54 | open |  |
| 11-24 19:02 | +15 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-24 19:02 | +10 | BTC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-24 19:02 | +5 | BTC | DOWN | 0.54 | 0.61 | 0.35 |
| 11-24 19:02 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-24 19:02 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-24 19:02 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-24 19:02 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 19:02 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 11-24 19:02 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 11-24 19:02 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-24 19:02 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-24 19:02 | +10 | ZEC | DOWN | 0.66 | open |  |
| 11-24 19:02 | +5 | ZEC | DOWN | 0.66 | open |  |
| 11-24 19:01 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 19:01 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-24 19:01 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-24 19:01 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-24 19:01 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.52 |
| 11-24 19:01 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 11-24 19:01 | +20 | DOGE | DOWN | 0.60 | open |  |
| 11-24 19:01 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-24 19:01 | +10 | DOGE | DOWN | 0.60 | open |  |
| 11-24 19:01 | +5 | DOGE | DOWN | 0.60 | 0.66 | 0.27 |
| 11-24 19:01 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.69 |
| 11-24 19:01 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-24 19:01 | +15 | ETH | DOWN | 0.60 | 0.78 | 1.50 |
| 11-24 19:01 | +10 | ETH | DOWN | 0.61 | 0.71 | 0.70 |
| 11-24 19:01 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 11-24 19:01 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
