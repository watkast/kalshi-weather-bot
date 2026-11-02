# Range-Scalp Bot

*Updated Mon Nov 02 01:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44167 | 38471 | 5696 (65) | 1 | $-12708.97 | -4.6% |
| **+10¢** | 32961 | 26375 | 6586 (86) | 1 | $-11485.70 | -5.5% |
| **+15¢** | 27587 | 20498 | 7089 (113) | 3 | $-10499.06 | -6.1% |
| **+20¢** | 24511 | 17089 | 7422 (147) | 3 | $-9233.41 | -6.0% |
| **+10¢ (15¢ stop)** | 53866 | 53780 | 86 (51) | 1 | $-20370.44 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 01:15 | +10 stop | NEAR | DOWN | 0.53 | 0.64 | 0.75 |
| 11-02 01:15 | +20 | NEAR | DOWN | 0.53 | open |  |
| 11-02 01:15 | +15 | NEAR | DOWN | 0.53 | open |  |
| 11-02 01:15 | +10 | NEAR | DOWN | 0.52 | 0.62 | 0.65 |
| 11-02 01:15 | +5 | NEAR | DOWN | 0.52 | 0.62 | 0.65 |
| 11-02 01:15 | +10 stop | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 11-02 01:15 | +20 | XRP | DOWN | 0.51 | open |  |
| 11-02 01:15 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-02 01:15 | +10 | XRP | DOWN | 0.51 | 0.61 | 0.65 |
| 11-02 01:15 | +5 | XRP | DOWN | 0.52 | 0.60 | 0.45 |
| 11-02 01:15 | +10 stop | HYPE | UP | 0.59 | open |  |
| 11-02 01:15 | +20 | HYPE | UP | 0.60 | open |  |
| 11-02 01:15 | +15 | HYPE | UP | 0.58 | open |  |
| 11-02 01:15 | +10 | HYPE | UP | 0.58 | open |  |
| 11-02 01:15 | +5 | HYPE | UP | 0.57 | open |  |
| 11-02 01:07 | +10 stop | HYPE | UP | 0.59 | 0.76 | 1.40 |
| 11-02 01:07 | +10 | HYPE | UP | 0.59 | 0.76 | 1.40 |
| 11-02 01:07 | +5 | HYPE | UP | 0.59 | 0.76 | 1.40 |
| 11-02 01:03 | +5 | XRP | UP | 0.70 | 0.87 | 1.47 |
| 11-02 01:03 | +5 | ETH | UP | 0.68 | 0.80 | 0.92 |
| 11-02 01:02 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
| 11-02 01:02 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 11-02 01:02 | +10 stop | SOL | UP | 0.63 | 0.82 | 1.62 |
| 11-02 01:02 | +20 | SOL | UP | 0.63 | 0.84 | 1.83 |
| 11-02 01:02 | +15 | SOL | UP | 0.63 | 0.82 | 1.62 |
| 11-02 01:02 | +10 | SOL | UP | 0.63 | 0.82 | 1.62 |
| 11-02 01:02 | +5 | SOL | UP | 0.63 | 0.82 | 1.62 |
| 11-02 01:02 | +5 | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 11-02 01:01 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 11-02 01:01 | +20 | XRP | UP | 0.61 | 0.87 | 2.35 |
| 11-02 01:01 | +15 | XRP | UP | 0.61 | 0.87 | 2.35 |
| 11-02 01:01 | +10 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-02 01:01 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-02 01:01 | +10 stop | DOGE | UP | 0.60 | 0.78 | 1.50 |
| 11-02 01:01 | +20 | DOGE | UP | 0.60 | 0.85 | 2.24 |
| 11-02 01:01 | +15 | DOGE | UP | 0.60 | 0.78 | 1.50 |
| 11-02 01:01 | +10 | DOGE | UP | 0.59 | 0.78 | 1.60 |
| 11-02 01:01 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 11-02 01:01 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-02 01:01 | +20 | ETH | UP | 0.58 | 0.80 | 1.90 |
